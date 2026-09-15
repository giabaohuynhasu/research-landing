import pytest
from sandbox import diff_report, ResearchObject

def test_diff_report_different_ids_raises_value_error():
    a = ResearchObject(id="a")
    b = ResearchObject(id="b")

    with pytest.raises(ValueError) as excinfo:
        diff_report(a, b)

    assert "diff_report compares two codings of the SAME object; got 'a' vs 'b'" in str(excinfo.value)
