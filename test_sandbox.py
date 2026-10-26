from sandbox import ResearchSandbox, ResearchObject, Revision, DeltaType

def test_order3_programme_report_zero_revisions():
    """Test order3_programme_report with an empty sandbox and with objects that have no revisions."""
    # Empty sandbox
    sandbox = ResearchSandbox()
    report = sandbox.order3_programme_report()

    assert report["total_revision_events"] == 0
    assert report["narrowed_or_withdrawn"] == 0
    assert report["reaffirmed_unchanged"] == 0
    assert report["extended_new_material"] == 0
    assert report["constraint_ratio"] is None
    assert report["reaffirmed_unchanged_cases"] == []

    # Sandbox with objects but no revisions
    sandbox_with_objs = ResearchSandbox(objects=[
        ResearchObject(id="obj1"),
        ResearchObject(id="obj2")
    ])
    report_with_objs = sandbox_with_objs.order3_programme_report()

    assert report_with_objs["total_revision_events"] == 0
    assert report_with_objs["narrowed_or_withdrawn"] == 0
    assert report_with_objs["reaffirmed_unchanged"] == 0
    assert report_with_objs["extended_new_material"] == 0
    assert report_with_objs["constraint_ratio"] is None
    assert report_with_objs["reaffirmed_unchanged_cases"] == []


def test_order3_programme_report_with_revisions():
    """Test order3_programme_report with multiple revisions across different objects."""
    obj1 = ResearchObject(id="obj1", revisions=[
        Revision(delta_type=DeltaType.NARROWED, trigger="t1"),
        Revision(delta_type=DeltaType.WITHDRAWN, trigger="t2"),
    ])

    obj2 = ResearchObject(id="obj2", revisions=[
        Revision(delta_type=DeltaType.REAFFIRMED, trigger="t3"),
        Revision(delta_type=DeltaType.REAFFIRMED, trigger="t4"),
        Revision(delta_type=DeltaType.EXTENDED, trigger="t5"),
    ])

    sandbox = ResearchSandbox(objects=[obj1, obj2])
    report = sandbox.order3_programme_report()

    assert report["total_revision_events"] == 5
    assert report["narrowed_or_withdrawn"] == 2 # 1 narrowed, 1 withdrawn
    assert report["reaffirmed_unchanged"] == 2
    assert report["extended_new_material"] == 1

    # constraint_ratio = narrowed_or_withdrawn / total_revision_events = 2 / 5 = 0.4
    assert report["constraint_ratio"] == 0.4

    assert report["reaffirmed_unchanged_cases"] == [
        {"paper": "obj2", "trigger": "t3"},
        {"paper": "obj2", "trigger": "t4"}
    ]
