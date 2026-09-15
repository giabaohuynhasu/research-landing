from sandbox import empty_template, ResearchObject

def test_empty_template():
    template = empty_template()
    assert "objects" in template

def test_research_object_creation():
    ro = ResearchObject(id="test_1", title="Test")
    assert ro.id == "test_1"
    assert ro.title == "Test"
