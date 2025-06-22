from letgo_edge.gears import RatioGear, GearClock

def test_ratiogear_fires():
    gear = RatioGear("test", 3)
    fired = [gear.tick(1) for _ in range(2)]
    assert fired == [False, False]
    assert gear.tick(1) == True
    assert gear.energy == 0

def test_gearclock_cascade():
    clock = GearClock([1, 3])
    firings = []
    for _ in range(10):
        firings.append(clock.tick())
    # Should see gear 1 fire every 3 ticks
    assert sum(1 for f in firings if 1 in f) == 3