import pytest
from unittest.mock import patch, MagicMock

from audit_engine import ThirdOrderAudit, SYSTEM_PROMPT


def test_third_order_audit_initialization():
    """Test that the ThirdOrderAudit client initializes correctly."""
    with patch("audit_engine.OpenAI") as mock_openai:
        api_key = "test_api_key"
        auditor = ThirdOrderAudit(api_key=api_key)

        mock_openai.assert_called_once_with(api_key=api_key)
        assert auditor.client == mock_openai.return_value


def test_third_order_audit_audit_method():
    """Test that the audit method calls OpenAI correctly and returns the result."""
    with patch("audit_engine.OpenAI") as mock_openai:
        api_key = "test_api_key"

        # Setup mock client
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        # Setup mock response
        mock_response = MagicMock()
        expected_output = "Audit completed successfully."
        mock_response.choices[0].message.content = expected_output
        mock_client.chat.completions.create.return_value = mock_response

        # Initialize auditor and run audit
        auditor = ThirdOrderAudit(api_key=api_key)
        paper_text = "This is a research paper text to audit."

        result = auditor.audit(paper_text)

        # Assert client was created
        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-5",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": paper_text
                }
            ],
            temperature=0
        )

        # Assert return value is correct
        assert result == expected_output


def test_third_order_audit_audit_method_exception():
    """Test that the audit method allows exceptions to bubble up when API call fails."""
    with patch("audit_engine.OpenAI") as mock_openai:
        api_key = "test_api_key"

        # Setup mock client to raise Exception
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_client.chat.completions.create.side_effect = Exception("API connection error")

        # Initialize auditor and run audit
        auditor = ThirdOrderAudit(api_key=api_key)
        paper_text = "This is a research paper text to audit."

        with pytest.raises(Exception, match="API connection error"):
            auditor.audit(paper_text)
