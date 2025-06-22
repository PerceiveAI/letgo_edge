from .handlers import fast_handler, medium_handler, deep_handler

gear_configs = [
    {"name": "Fast",   "threshold": 1,  "handler": fast_handler, "log": True},
    {"name": "Medium", "threshold": 5,  "handler": medium_handler, "log": True},
    {"name": "Deep",   "threshold": 12, "handler": deep_handler, "log": True},
]