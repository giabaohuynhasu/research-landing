import numpy as np
import pytest
from alrp_simulation_model import solve_t_star

def test_solve_t_star_before_evo2():
    # Setup parameters so that t* is reached before t_evo2
    lambda_bzm0 = 1.0
    r_A = 1.0
    lambda_gen0 = 0.5
    r_gen = 1.0
    t_evo2 = 2.0

    # We want t* = 1.0, which is < t_evo2 (2.0)
    # The analytic solution for t < t_evo2 is t = ln(mu_prime / lambda_bzm0) / r_A
    # mu_prime = lambda_bzm0 * exp(r_A * t) = 1.0 * exp(1.0 * 1.0) = exp(1)
    mu_prime = np.exp(1)

    t_star = solve_t_star(lambda_bzm0, r_A, lambda_gen0, r_gen, t_evo2, mu_prime)

    # Assert that the solved t* is close to 1.0
    assert np.isclose(t_star, 1.0, atol=1e-5), f"Expected 1.0, got {t_star}"


def test_solve_t_star_after_evo2():
    # Setup parameters so that t* is reached after t_evo2
    lambda_bzm0 = 1.0
    r_A = 1.0
    lambda_gen0 = 1.0
    r_gen = 1.0
    t_evo2 = 0.0

    # We want t* = 1.0, which is > t_evo2 (0.0)
    # Since r_A = r_gen = 1.0 and t_evo2 = 0.0:
    # lambda_total(t) = exp(t) + exp(t) = 2 * exp(t)
    # mu_prime = 2 * exp(1.0)
    mu_prime = 2 * np.exp(1)

    t_star = solve_t_star(lambda_bzm0, r_A, lambda_gen0, r_gen, t_evo2, mu_prime)

    # Assert that the solved t* is close to 1.0
    assert np.isclose(t_star, 1.0, atol=1e-5), f"Expected 1.0, got {t_star}"


def test_solve_t_star_exact_evo2():
    # Test scenario where t* is exactly at t_evo2
    lambda_bzm0 = 1.0
    r_A = 1.0
    lambda_gen0 = 0.5
    r_gen = 1.0
    t_evo2 = 1.0

    # If t* = 1.0, it is not strictly > t_evo2, so val_gen = 0
    # mu_prime = lambda_bzm0 * exp(r_A * 1.0) = exp(1)
    mu_prime = np.exp(1)

    t_star = solve_t_star(lambda_bzm0, r_A, lambda_gen0, r_gen, t_evo2, mu_prime)

    assert np.isclose(t_star, 1.0, atol=1e-5), f"Expected 1.0, got {t_star}"


@pytest.mark.parametrize("mu_prime", [2.25, 7.5, 22.5])
def test_solve_t_star_numerical_convergence(mu_prime):
    # Use parameters from the actual simulation
    lambda_bzm0 = 0.5
    r_A = 1.85
    lambda_gen0 = 0.15
    r_gen = 2.2
    t_evo2 = 0.15

    t_star = solve_t_star(lambda_bzm0, r_A, lambda_gen0, r_gen, t_evo2, mu_prime)

    # Plug t_star back into the equation
    val_bzm = lambda_bzm0 * np.exp(r_A * t_star)
    val_gen = 0.0
    if t_star > t_evo2:
        val_gen = lambda_gen0 * np.exp(r_gen * (t_star - t_evo2))

    lambda_total = val_bzm + val_gen

    # Assert that lambda_total(t*) converges to mu_prime
    assert np.isclose(lambda_total, mu_prime, atol=1e-5), f"Expected {mu_prime}, got {lambda_total}"
