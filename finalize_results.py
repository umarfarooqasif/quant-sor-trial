import json

# Load optimized results
with open("output.json", "r") as f:
    optimized_result = json.load(f)

# Load baseline results
with open("baselines.json", "r") as f:
    baselines = json.load(f)

optimized_cash = optimized_result["optimized"]["total_cash"]

# Calculate bps savings = (baseline - optimized) / baseline * 10000
bps = {
    k: round((v["total_cash"] - optimized_cash) / v["total_cash"] * 10000, 2)
    for k, v in baselines.items()
}

# Create final structure
final_json = {
    "best_parameters": optimized_result["best_parameters"],
    "optimized": optimized_result["optimized"],
    "baselines": baselines,
    "savings_vs_baselines_bps": bps
}

# Save final output
with open("final_result.json", "w") as f:
    json.dump(final_json, f, indent=2)

# Print nicely
print(json.dumps(final_json, indent=2))
