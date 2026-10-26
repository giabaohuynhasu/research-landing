import pytest
from sandbox import ResearchObject, FalsificationCondition

def test_order1_pass_empty():
    obj = ResearchObject(id="ro1", falsification_conditions=[])
    assert obj.order1_pass() is False

def test_order2_pass_empty():
    obj = ResearchObject(id="ro1", falsification_conditions=[])
    assert obj.order2_pass() is False

def test_order1_pass_with_conditions():
    fc = FalsificationCondition(id="fc1", references_external_source=False)
    obj = ResearchObject(id="ro1", falsification_conditions=[fc])
    assert obj.order1_pass() is True

def test_order2_pass_no_external_source():
    fc = FalsificationCondition(id="fc1", references_external_source=False)
    obj = ResearchObject(id="ro1", falsification_conditions=[fc])
    assert obj.order2_pass() is False

def test_order2_pass_with_external_source():
    fc = FalsificationCondition(id="fc1", references_external_source=True)
    obj = ResearchObject(id="ro1", falsification_conditions=[fc])
    assert obj.order2_pass() is True

def test_order2_pass_mixed_sources():
    fc1 = FalsificationCondition(id="fc1", references_external_source=False)
    fc2 = FalsificationCondition(id="fc2", references_external_source=True)
    obj = ResearchObject(id="ro1", falsification_conditions=[fc1, fc2])
    assert obj.order2_pass() is True
