import sandbox


def test_sandbox_template():
    template = sandbox.empty_template()
    assert "objects" in template
    assert len(template["objects"]) > 0
    assert template["objects"][0]["id"] == "example_paper_id"
