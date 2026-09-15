import pytest
import numpy as np
from alrp_simulation_model import run_simulation_paths

def test_run_simulation_paths_default():
    """Test the happy path with default parameters."""
    time_grid, lambda_total, lambda_bzm, lambda_gen, results = run_simulation_paths(num_paths=2, t_max=0.1, dt=0.01)

    assert len(time_grid) > 0
    assert len(lambda_total) == len(time_grid)
    assert len(lambda_bzm) == len(time_grid)
    assert len(lambda_gen) == len(time_grid)

    assert len(results) == 3
    for key, val in results.items():
        assert "paths" in val
        assert val["paths"].shape == (2, len(time_grid))

def test_run_simulation_paths_zero_paths():
    """Test that zero num_paths raises a ValueError."""
    with pytest.raises(ValueError, match="num_paths must be strictly positive"):
        run_simulation_paths(num_paths=0, t_max=0.1, dt=0.01)

def test_run_simulation_paths_negative_paths():
    """Test that negative num_paths raises a ValueError."""
    with pytest.raises(ValueError, match="num_paths must be strictly positive"):
        run_simulation_paths(num_paths=-5, t_max=0.1, dt=0.01)

def test_run_simulation_paths_zero_t_max():
    """Test that zero t_max raises a ValueError."""
    with pytest.raises(ValueError, match="t_max must be strictly positive"):
        run_simulation_paths(num_paths=2, t_max=0.0, dt=0.01)

def test_run_simulation_paths_negative_t_max():
    """Test that negative t_max raises a ValueError."""
    with pytest.raises(ValueError, match="t_max must be strictly positive"):
        run_simulation_paths(num_paths=2, t_max=-1.0, dt=0.01)

def test_run_simulation_paths_zero_dt():
    """Test that zero dt raises a ValueError."""
    with pytest.raises(ValueError, match="dt must be strictly positive"):
        run_simulation_paths(num_paths=2, t_max=0.1, dt=0.0)

def test_run_simulation_paths_negative_dt():
    """Test that negative dt raises a ValueError."""
    with pytest.raises(ValueError, match="dt must be strictly positive"):
        run_simulation_paths(num_paths=2, t_max=0.1, dt=-0.01)
