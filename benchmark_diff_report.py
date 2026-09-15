import time
import timeit
from sandbox import ResearchObject, FalsificationCondition, Revision, DeltaType, diff_report

def setup_data():
    a = ResearchObject(
        id="test_obj",
        title="Test Obj",
        falsification_conditions=[FalsificationCondition(id="f1", references_external_source=True)],
        revisions=[Revision(delta_type=DeltaType.NARROWED, trigger="test")]
    )
    b = ResearchObject(
        id="test_obj",
        title="Test Obj",
        falsification_conditions=[FalsificationCondition(id="f1", references_external_source=False)],
        revisions=[Revision(delta_type=DeltaType.REAFFIRMED, trigger="test2")]
    )
    return a, b

def run_benchmark():
    a, b = setup_data()
    # Warmup
    for _ in range(100):
        diff_report(a, b)

    # Run
    start_time = time.perf_counter_ns()
    for _ in range(100000):
        diff_report(a, b)
    end_time = time.perf_counter_ns()

    return (end_time - start_time) / 100000

if __name__ == "__main__":
    ns_per_call = run_benchmark()
    print(f"Average time per diff_report call: {ns_per_call:.2f} ns")
