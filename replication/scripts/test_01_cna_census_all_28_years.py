import unittest
import json
import importlib.util
import sys
import os

# Dynamically import the module because its name starts with a number
module_path = os.path.join(os.path.dirname(__file__), '01_cna_census_all_28_years.py')
spec = importlib.util.spec_from_file_location("cna_census", module_path)
cna_census = importlib.util.module_from_spec(spec)
sys.modules["cna_census"] = cna_census
spec.loader.exec_module(cna_census)

extract_cve_info = cna_census.extract_cve_info

class TestExtractCveInfo(unittest.TestCase):
    def _to_bytes(self, data):
        return json.dumps(data).encode('utf-8')

    def test_extract_assigner_short_name(self):
        data = {
            "cveMetadata": {
                "state": "PUBLISHED",
                "assignerShortName": "mitre"
            }
        }
        state, assigner = extract_cve_info(self._to_bytes(data))
        self.assertEqual(state, "PUBLISHED")
        self.assertEqual(assigner, "mitre")

    def test_extract_assigner_org_id_fallback(self):
        data = {
            "cveMetadata": {
                "state": "PUBLISHED",
                "assignerOrgId": "org-123"
            }
        }
        state, assigner = extract_cve_info(self._to_bytes(data))
        self.assertEqual(state, "PUBLISHED")
        self.assertEqual(assigner, "org-123")

    def test_extract_cna_short_name_fallback(self):
        data = {
            "cveMetadata": {
                "state": "REJECTED"
            },
            "containers": {
                "cna": {
                    "providerMetadata": {
                        "shortName": "cna-short"
                    }
                }
            }
        }
        state, assigner = extract_cve_info(self._to_bytes(data))
        self.assertEqual(state, "REJECTED")
        self.assertEqual(assigner, "cna-short")

    def test_extract_cna_org_id_fallback(self):
        data = {
            "cveMetadata": {
                "state": "PUBLISHED"
            },
            "containers": {
                "cna": {
                    "providerMetadata": {
                        "orgId": "cna-org-123"
                    }
                }
            }
        }
        state, assigner = extract_cve_info(self._to_bytes(data))
        self.assertEqual(state, "PUBLISHED")
        self.assertEqual(assigner, "cna-org-123")

    def test_empty_structures_default_values(self):
        data = {}
        state, assigner = extract_cve_info(self._to_bytes(data))
        self.assertEqual(state, "PUBLISHED")
        self.assertEqual(assigner, "UNKNOWN")

    def test_invalid_json(self):
        raw_bytes = b"invalid json"
        state, assigner = extract_cve_info(raw_bytes)
        self.assertEqual(state, "ERROR")
        self.assertEqual(assigner, "UNKNOWN")

if __name__ == '__main__':
    unittest.main()