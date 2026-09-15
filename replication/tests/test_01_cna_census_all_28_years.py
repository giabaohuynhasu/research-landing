import pytest
import importlib

# The module name starts with a number so we must use importlib
cna_census = importlib.import_module("replication.scripts.01_cna_census_all_28_years")
extract_cve_info = cna_census.extract_cve_info

def test_extract_cve_info_invalid_json():
    """Test that extract_cve_info gracefully handles invalid JSON bytes."""
    invalid_bytes = b'invalid json'
    state, assigner = extract_cve_info(invalid_bytes)
    assert state == "ERROR"
    assert assigner == "UNKNOWN"

def test_extract_cve_info_valid_json():
    """Test that extract_cve_info correctly extracts info from valid JSON."""
    valid_json_bytes = b'{"cveMetadata": {"state": "PUBLISHED", "assignerShortName": "mitre"}}'
    state, assigner = extract_cve_info(valid_json_bytes)
    assert state == "PUBLISHED"
    assert assigner == "mitre"
