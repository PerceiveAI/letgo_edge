from config import gear_configs
from scheduler import ModularLetGoScheduler

if __name__ == "__main__":
    queries = [f"Query {i+1}" for i in range(24)]
    sched = ModularLetGoScheduler(gear_configs)
    for tick, query in enumerate(queries):
        sched.tick(query)