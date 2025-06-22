class RatioGear:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold
        self.energy = 0
    def tick(self, signal=1):
        self.energy += signal
        if self.energy >= self.threshold:
            self.energy = 0
            return True
        return False

class GearClock:
    def __init__(self, thresholds):
        self.gears = [RatioGear(f"wheel_{i}", t) for i, t in enumerate(thresholds)]
    def tick(self):
        fired = []
        carry = 1
        for i, gear in enumerate(self.gears):
            if gear.tick(carry):
                fired.append(i)
                carry = 1
            else:
                carry = 0
            if carry == 0: break
        return fired