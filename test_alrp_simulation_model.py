import pytest
import numpy as np
from alrp_simulation_model import SimulationParams, solve_t_star

def test_solve_t_star():
    # Set up some known parameters
    params = SimulationParams(
        lambda_bzm0 = 0.5,
        r_A = 1.85,
        lambda_gen0 = 0.15,
        r_gen = 2.2,
        t_evo2 = 0.15
    )
    mu_prime = 1.5 * 1.5

    t_star = solve_t_star(params, mu_prime)

    assert isinstance(t_star, float)
    assert t_star > 0
