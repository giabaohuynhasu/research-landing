import pytest
import audit_engine

def test_system_prompt_loaded():
    assert audit_engine.SYSTEM_PROMPT is not None
    assert len(audit_engine.SYSTEM_PROMPT) > 0
    assert "structural auditor for research papers" in audit_engine.SYSTEM_PROMPT

def test_third_order_audit_init():
    auditor = audit_engine.ThirdOrderAudit(api_key="test_key")
    assert auditor.client is not None
    assert auditor.client.api_key == "test_key"
