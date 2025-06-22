from letgo_edge.gears import RatioGear

def simulate_googol_gear(num_wheels=100, ratio=10, num_ticks=2000):
    gears = [RatioGear(f"wheel_{i}", threshold=(1 if i == 0 else ratio)) for i in range(num_wheels)]
    first_fire = {g.name: None for g in gears}
    for t in range(num_ticks):
        sig = 1  # external signal
        fired = [False] * num_wheels
        fired[0] = gears[0].tick(sig)
        if fired[0] and first_fire[gears[0].name] is None:
            first_fire[gears[0].name] = t
        for i in range(1, num_wheels):
            fired[i] = gears[i].tick(1 if fired[i-1] else 0)
            if fired[i] and first_fire[gears[i].name] is None:
                first_fire[gears[i].name] = t
    print("First fire tick per gear (truncated):")
    for i in range(min(num_wheels, 20)):
        print(f"{gears[i].name:>10} fired at tick {first_fire[gears[i].name]}")
    # Show only first 20 wheels for brevity

if __name__ == "__main__":
    simulate_googol_gear(num_wheels=20, ratio=10, num_ticks=200000)
    # Note: To see wheel_10+ fire, you'll need even more ticks!