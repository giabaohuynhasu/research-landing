import numpy as np
import matplotlib.pyplot as plt
import os

# Set matplotlib to non-interactive mode
import matplotlib
matplotlib.use('Agg')

def solve_t_star(lambda_bzm0, r_A, lambda_gen0, r_gen, t_evo2, mu_prime):
    """
    Solve for the instability threshold t* numerically where lambda_total(t*) = mu_prime.
    """
    from scipy.optimize import fsolve
    
    def equations(t):
        t_val = t[0]
        val_bzm = lambda_bzm0 * np.exp(r_A * t_val)
        val_gen = 0.0
        if t_val > t_evo2:
            val_gen = lambda_gen0 * np.exp(r_gen * (t_val - t_evo2))
        return [val_bzm + val_gen - mu_prime]
    
    # Initial guess
    t_guess = [np.log(max(0.1, mu_prime / lambda_bzm0)) / r_A]
    t_star_solved = fsolve(equations, t_guess)[0]
    return t_star_solved

def run_simulation_paths(num_paths=100, t_max=4.0, dt=0.001, seed=42):
    """
    Simulates the ALRP Workload Process Delta(t) over multiple Monte Carlo paths.
    """
    np.random.seed(seed)
    
    # Parameters
    lambda_bzm0 = 0.5      # Baseline BZM arrival rate (events/year)
    r_A = 1.85             # ARSI capability growth rate (year^-1)
    lambda_gen0 = 0.15     # Baseline de novo generative arrival rate
    r_gen = 2.2            # Growth rate of de novo generation
    t_evo2 = 0.15          # Evo 2 event (Aug 2026, ~0.15 years from June 2026 baseline)
    
    # Jump size distribution (Lognormal)
    e_delta = 1.5
    var_delta = 0.25
    sigma_sq = np.log(var_delta / (e_delta**2) + 1)
    mu_log = np.log(e_delta) - sigma_sq / 2
    sigma_log = np.sqrt(sigma_sq)
    
    # Scenarios for diffusion capacity mu' (event-equivalents/yr)
    scenarios = {
        "Modest Capacity (mu'=1.5)": 1.5 * e_delta,    # mu = mu' * E[delta]
        "Expanded Capacity (mu'=5.0)": 5.0 * e_delta,
        "High Capacity (mu'=15.0)": 15.0 * e_delta
    }
    
    time_grid = np.arange(0, t_max + dt, dt)
    n_steps = len(time_grid)
    
    # Pre-calculate arrival rates on grid
    lambda_bzm = lambda_bzm0 * np.exp(r_A * time_grid)
    lambda_gen = np.zeros_like(time_grid)
    mask_gen = time_grid > t_evo2
    lambda_gen[mask_gen] = lambda_gen0 * np.exp(r_gen * (time_grid[mask_gen] - t_evo2))
    lambda_total = lambda_bzm + lambda_gen
    
    results = {}
    
    for label, mu_val in scenarios.items():
        paths_delta = np.zeros((num_paths, n_steps))
        
        initial_gap = 7.3  # DunedinPACE socioeconomic gradient baseline
        
        for p in range(num_paths):
            delta = initial_gap
            paths_delta[p, 0] = delta
            for step in range(1, n_steps):
                t = time_grid[step - 1]
                
                # Check for Poisson event
                rate = lambda_total[step - 1]
                prob_event = rate * dt
                
                event_occurred = np.random.rand() < prob_event
                jump = 0.0
                if event_occurred:
                    jump = np.random.lognormal(mu_log, sigma_log)
                
                # Update workload process Delta(t)
                delta = max(0.0, delta - mu_val * dt) + jump
                paths_delta[p, step] = delta
                
        # Calculate quantiles
        mean_path = np.mean(paths_delta, axis=0)
        p25 = np.percentile(paths_delta, 25, axis=0)
        p75 = np.percentile(paths_delta, 75, axis=0)
        p05 = np.percentile(paths_delta, 5, axis=0)
        p95 = np.percentile(paths_delta, 95, axis=0)
        
        # Calculate t*
        mu_prime = mu_val / e_delta
        t_star = solve_t_star(lambda_bzm0, r_A, lambda_gen0, r_gen, t_evo2, mu_prime)
        
        results[label] = {
            "paths": paths_delta,
            "mean": mean_path,
            "p25": p25,
            "p75": p75,
            "p05": p05,
            "p95": p95,
            "t_star": t_star,
            "mu_prime": mu_prime
        }
        
    return time_grid, lambda_total, lambda_bzm, lambda_gen, results

def plot_alrp_dynamics(time_grid, lambda_total, lambda_bzm, lambda_gen, results, output_path):
    """
    Generates a high-quality visualization of the ALRP queueing dynamics under Evo 2 de novo expansion.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 10), sharex=True)
    
    # 1. Plot Arrival Rates vs Diffusion Capacity
    ax1.plot(time_grid, lambda_bzm, label="Baseline discovery rate (AI-accelerated)", color="#2b5c8f", linestyle="--", linewidth=1.8)
    ax1.plot(time_grid, lambda_gen, label="De-novo generative rate (Evo 2)", color="#d95f02", linestyle=":", linewidth=1.8)
    ax1.plot(time_grid, lambda_total, label="Total discovery rate λ(t)", color="#7570b3", linewidth=2.5)
    
    # Draw horizontal lines for mu'
    colors_mu = ["#e7298a", "#1b9e77", "#66a61e"]
    for i, (label, res) in enumerate(results.items()):
        mu_prime = res["mu_prime"]
        t_star = res["t_star"]
        color = colors_mu[i]
        
        ax1.axhline(y=mu_prime, color=color, linestyle="-.", label=f"Diffusion capacity μ': {label.split(' ')[0]}", alpha=0.8)
        if t_star < time_grid[-1]:
            ax1.axvline(x=t_star, color=color, linestyle="--", alpha=0.6)
            ax1.plot(t_star, mu_prime, marker="o", color=color, markersize=8)
            ax1.text(t_star + 0.05, mu_prime + 0.2, f"t* = {t_star:.2f} years", color=color, fontweight="bold", fontsize=9)
            
    ax1.set_ylabel("Event rate (events / year)", fontsize=11, fontweight="bold")
    ax1.set_title("Frontier growth dynamics and ALRP queueing instability threshold", fontsize=12, fontweight="bold", pad=15)
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="none", shadow=False, fontsize=9)
    
    # Annotate Evo 2 Event
    ax1.axvline(x=0.15, color="red", linestyle="-", alpha=0.3)
    ax1.text(0.17, 0.2, "Evo 2 announcement (06/08/2026)", color="red", fontsize=9, alpha=0.8)
    
    # 2. Plot Asymmetry Gap Delta(t) Simulation Paths
    for i, (label, res) in enumerate(results.items()):
        color = colors_mu[i]
        ax2.plot(time_grid, res["mean"], label=f"Expected gap Δ(t) - {label.split(' ')[0]}", color=color, linewidth=2)
        ax2.fill_between(time_grid, res["p25"], res["p75"], color=color, alpha=0.15)
        ax2.fill_between(time_grid, res["p05"], res["p95"], color=color, alpha=0.05, linestyle=":")
        
    ax2.axhline(y=7.3, color="gray", linestyle="--", alpha=0.5, label="DunedinPACE baseline (7.3 years)")
    ax2.set_xlabel("Time since baseline 06/2026 (years)", fontsize=11, fontweight="bold")
    ax2.set_ylabel("Asymmetry gap Δ(t) (years of healthy life)", fontsize=11, fontweight="bold")
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="none", shadow=False, fontsize=9)
    ax2.set_ylim(bottom=0)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Plot saved successfully to {output_path}")

if __name__ == "__main__":
    # Ensure scratch directory exists
    os.makedirs("/workspace/scratch/alrp-simulation", exist_ok=True)
    
    print("Running ALRP Queueing Simulation...")
    time_grid, lambda_total, lambda_bzm, lambda_gen, results = run_simulation_paths()
    
    # Save chart in scratch
    chart_path = "/workspace/scratch/alrp-simulation/alrp_simulation_chart.png"
    plot_alrp_dynamics(time_grid, lambda_total, lambda_bzm, lambda_gen, results, chart_path)
    
    # Print numerical results summary
    print("\nSimulation Results Summary:")
    for label, res in results.items():
        print(f"Scenario: {label}")
        print(f"  Diffusion Capacity mu': {res['mu_prime']:.2f} event-equivalents/yr")
        print(f"  Solved Instability Threshold t*: {res['t_star']:.2f} years from baseline (June 2026)")
        print(f"  Mean Gap Delta at t=1.0 yr: {res['mean'][int(1.0/0.001)]:.2f} years")
        print(f"  Mean Gap Delta at t=3.0 yr: {res['mean'][int(3.0/0.001)]:.2f} years")
        print("-" * 50)
