from letgo_edge.scheduler import ModularLetGoScheduler
from letgo_edge.handlers import fast_handler

def test_scheduler_fires_correctly():
    cfg = [{"name":"Fast","threshold":1,"handler":fast_handler}]
    sched = ModularLetGoScheduler(cfg)
    calls = []
    def handler(q):
        calls.append(q)
        return "done"
    sched.handlers[0] = handler
    for i in range(5):
        sched.tick(f"q{i}")
    assert calls == ["q0","q1","q2","q3","q4"]