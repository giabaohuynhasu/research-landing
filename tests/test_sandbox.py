import json
from sandbox import ResearchObject, FalsificationCondition, Revision, DeltaType

def test_research_object_serialization():
    # Setup test object with properties
    fc1 = FalsificationCondition(
        id="fc_1",
        text="A specific claim",
        references_external_source=True,
        source_note="Tested against reality"
    )
    fc2 = FalsificationCondition(
        id="fc_2",
        text="Another specific claim",
        references_external_source=False,
        source_note="Noted in the text"
    )

    rev1 = Revision(
        delta_type=DeltaType.NARROWED,
        trigger="A critique",
        note="Clarified the scope",
        source_note="Criticism from peer review"
    )
    rev2 = Revision(
        delta_type=DeltaType.WITHDRAWN,
        trigger="A falsification",
        note="Retracted the claim",
        source_note="Own testing"
    )

    ro = ResearchObject(
        id="ro_1",
        title="A test research object",
        falsification_conditions=[fc1, fc2],
        revisions=[rev1, rev2],
        self_referential_audit_present=True
    )

    # Serialize to dictionary
    d = ro.to_dict()

    # Optional: simulate round trip through JSON
    json_str = json.dumps(d)
    d_loaded = json.loads(json_str)

    # Deserialize back to object
    ro_deserialized = ResearchObject.from_dict(d_loaded)

    # Assert equivalence
    assert ro_deserialized.id == ro.id
    assert ro_deserialized.title == ro.title
    assert ro_deserialized.self_referential_audit_present == ro.self_referential_audit_present

    assert len(ro_deserialized.falsification_conditions) == 2
    assert ro_deserialized.falsification_conditions[0].id == "fc_1"
    assert ro_deserialized.falsification_conditions[0].text == "A specific claim"
    assert ro_deserialized.falsification_conditions[0].references_external_source == True
    assert ro_deserialized.falsification_conditions[0].source_note == "Tested against reality"

    assert ro_deserialized.falsification_conditions[1].id == "fc_2"
    assert ro_deserialized.falsification_conditions[1].text == "Another specific claim"
    assert ro_deserialized.falsification_conditions[1].references_external_source == False
    assert ro_deserialized.falsification_conditions[1].source_note == "Noted in the text"

    assert len(ro_deserialized.revisions) == 2
    assert ro_deserialized.revisions[0].delta_type == DeltaType.NARROWED
    assert ro_deserialized.revisions[0].trigger == "A critique"
    assert ro_deserialized.revisions[0].note == "Clarified the scope"
    assert ro_deserialized.revisions[0].source_note == "Criticism from peer review"

    assert ro_deserialized.revisions[1].delta_type == DeltaType.WITHDRAWN
    assert ro_deserialized.revisions[1].trigger == "A falsification"
    assert ro_deserialized.revisions[1].note == "Retracted the claim"
    assert ro_deserialized.revisions[1].source_note == "Own testing"

    # Ensure dataclass equality works as expected
    assert ro == ro_deserialized


def test_research_object_serialization_empty():
    ro = ResearchObject(id="ro_empty")

    # Serialize to dictionary
    d = ro.to_dict()

    # Optional: simulate round trip through JSON
    json_str = json.dumps(d)
    d_loaded = json.loads(json_str)

    # Deserialize back to object
    ro_deserialized = ResearchObject.from_dict(d_loaded)

    assert ro_deserialized.id == "ro_empty"
    assert ro_deserialized.title == ""
    assert ro_deserialized.falsification_conditions == []
    assert ro_deserialized.revisions == []
    assert ro_deserialized.self_referential_audit_present == False

    assert ro == ro_deserialized
