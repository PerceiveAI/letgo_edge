from letgo_edge.config import gear_configs
from letgo_edge.scheduler import ModularLetGoScheduler

import time
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    queries = [
        "What is the capital of France?",
        "Explain AI in one sentence.",
        "Write a haiku about the moon.",
        "Summarize the plot of Hamlet.",
        "Generate Python code for a Fibonacci sequence.",
        "Translate 'How are you?' to Spanish.",
        "Describe gravitational lensing in cosmology.",
        "Tell a joke about robots.",
        "Write an email apologizing for a late delivery.",
        "Draft a business plan for a coffee shop.",
        "What's the weather in Tokyo?",
        "Explain how gears work in simple terms.",
        "Write a motivational quote.",
        "Summarize the news about AI in 2023.",
        "Draft a product pitch for a phase-based AI router.",
    ]
    sched = ModularLetGoScheduler(gear_configs)
    records = []
    for tick, query in enumerate(queries):
        start = time.time()
        fired = sched.tick(query)
        elapsed = time.time() - start
        for i in fired:
            gear_name = gear_configs[i]["name"]
            records.append({"tick": tick, "gear": gear_name, "query": query, "elapsed": elapsed})
    # Plot usage
    df = pd.DataFrame(records)
    plt.figure(figsize=(7,4))
    df["gear"].value_counts().plot.pie(autopct='%1.1f%%', title="Gear Usage (Phase-Scheduled)")
    plt.ylabel("")
    plt.show()
    plt.figure(figsize=(7,4))
    df.groupby("gear")["elapsed"].mean().plot.bar(color=["#2196F3","#4CAF50","#E53935"])
    plt.title("Avg Handler Time per Gear")
    plt.ylabel("Seconds")
    plt.show()