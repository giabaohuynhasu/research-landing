import json
import importlib.util
import pytest
from pathlib import Path

# Dynamically import the script since it starts with a number
script_path = Path(__file__).parent / "01_cna_census_all_28_years.py"
spec = importlib.util.spec_from_file_location("cna_census", script_path)
cna_census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cna_census)

extract_cve_info = cna_census.extract_cve_info

def to_bytes(data):
    return json.dumps(data).encode("utf-8")

def test_valid_json_assigner_short_name():
    data = {
        "cveMetadata": {
            "assignerShortName": "mitre"
        }
    }
    assert extract_cve_info(to_bytes(data)) == ("PUBLISHED", "mitre")

def test_valid_json_assigner_org_id():
    data = {
        "cveMetadata": {
            "assignerOrgId": "org-123"
        }
    }
    assert extract_cve_info(to_bytes(data)) == ("PUBLISHED", "org-123")

def test_valid_json_cna_short_name():
    data = {
        "containers": {
            "cna": {
                "providerMetadata": {
                    "shortName": "cna-short"
                }
            }
        }
    }
    assert extract_cve_info(to_bytes(data)) == ("PUBLISHED", "cna-short")

def test_valid_json_cna_org_id():
    data = {
        "containers": {
            "cna": {
                "providerMetadata": {
                    "orgId": "cna-org-id"
                }
            }
        }
    }
    assert extract_cve_info(to_bytes(data)) == ("PUBLISHED", "cna-org-id")

def test_unknown_assigner():
    data = {}
    assert extract_cve_info(to_bytes(data)) == ("PUBLISHED", "UNKNOWN")

def test_state_fallback():
    data = {
        "cveMetadata": {
            "assignerShortName": "mitre"
        }
    }
    assert extract_cve_info(to_bytes(data)) == ("PUBLISHED", "mitre")

def test_state_explicit():
    data = {
        "cveMetadata": {
            "state": "REJECTED",
            "assignerShortName": "mitre"
        }
    }
    assert extract_cve_info(to_bytes(data)) == ("REJECTED", "mitre")

def test_invalid_json():
    assert extract_cve_info(b"invalid json") == ("ERROR", "UNKNOWN")

def test_unexpected_json_type():
    assert extract_cve_info(b"[]") == ("ERROR", "UNKNOWN")
