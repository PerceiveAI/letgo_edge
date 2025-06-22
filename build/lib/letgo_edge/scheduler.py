from .gears import RatioGear

class ModularLetGoScheduler:
    def __init__(self, gear_configs):
        self.gears = [RatioGear(cfg["name"], cfg["threshold"]) for cfg in gear_configs]
        self.handlers = [cfg["handler"] for cfg in gear_configs]
        self.configs = gear_configs
    def tick(self, *args, **kwargs):
        fired = []
        carry = 1
        for i, gear in enumerate(self.gears):
            if gear.tick(carry):
                out = self.handlers[i](*args, **kwargs)
                if self.configs[i].get("log"):
                    print(f"{gear.name} fired: {out}")
                carry = 1
                fired.append(i)
            else:
                carry = 0
            if carry == 0: break
        return fired