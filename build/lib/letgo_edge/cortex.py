class LetEdgeCortex:
    def __init__(self):
        self.handlers = {}
    def register(self, name, handler):
        self.handlers[name] = handler
    def tick(self, tick_num=0, signal_type=None, payload=None):
        if signal_type and signal_type in self.handlers:
            return self.handlers[signal_type](payload or {})
        else:
            out = {}
            for name, handler in self.handlers.items():
                out[name] = handler(payload or {})
            return out