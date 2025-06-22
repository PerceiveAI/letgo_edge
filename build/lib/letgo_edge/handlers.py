import time

def fast_handler(query):
    time.sleep(1 + 0.1 * hash(query) % 3)
    return f"[FAST] {query}"

def medium_handler(query):
    time.sleep(4 + 0.2 * hash(query) % 3)
    return f"[MEDIUM] {query}"

def deep_handler(query):
    time.sleep(10 + 0.5 * hash(query) % 3)
    return f"[DEEP] {query}"