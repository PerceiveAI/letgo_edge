import time
from letgo_edge.gears import GearClock

def test_gearclock_speed():
    clock = GearClock([1,10,100])
    N = 10000
    start = time.perf_counter()
    for _ in range(N):
        clock.tick()
    elapsed = time.perf_counter() - start
    # Should be much less than N*number_of_gears calls if phase works!
    assert elapsed < 1.5  # This should pass on modern machines