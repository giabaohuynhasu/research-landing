import pytest
import importlib.util
import sys
from pathlib import Path

# Load module dynamically because its name starts with a number
module_name = 'cna_census'
file_path = Path('replication/scripts/01_cna_census_all_28_years.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
cna_census = importlib.util.module_from_spec(spec)
sys.modules[module_name] = cna_census
spec.loader.exec_module(cna_census)

def test_extract_year_from_filename():
    assert cna_census.extract_year_from_filename("cves/2021/CVE-2021-1234.json") == 2021
    assert cna_census.extract_year_from_filename("not_a_json_file.txt") is None
    assert cna_census.extract_year_from_filename("cves/CVE-2021-1234.json") is None
    assert cna_census.extract_year_from_filename("other/2021/CVE-2021-1234.json") is None
