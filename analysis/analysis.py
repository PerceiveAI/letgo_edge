import matplotlib.pyplot as plt

def plot_gear_usage(results):
    from collections import Counter
    gear_counts = Counter(r["gear"] for r in results)
    plt.bar(gear_counts.keys(), gear_counts.values())
    plt.title("Gear Usage Frequency")
    plt.xlabel("Gear")
    plt.ylabel("Count")
    plt.show()