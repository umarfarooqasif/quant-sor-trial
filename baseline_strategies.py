import pandas as pd
import json
from datetime import datetime, timedelta

CSV_PATH = "l1_day.csv"
ORDER_SIZE = 5000

# Load and preprocess
df = pd.read_csv(CSV_PATH, parse_dates=["ts_event"])
df = df[(df["ts_event"] >= "2024-08-01T13:36:32") & (df["ts_event"] <= "2024-08-01T13:45:14")]
df.sort_values("ts_event", inplace=True)

def simulate_best_ask(df):
    filled = 0
    cost = 0.0
    for _, row in df.iterrows():
        ask = row["ask_px_00"]
        size = row["ask_sz_00"]
        to_buy = min(size, ORDER_SIZE - filled)
        cost += to_buy * ask
        filled += to_buy
        if filled >= ORDER_SIZE:
            break
    return {"total_cash": cost, "avg_fill_px": round(cost / ORDER_SIZE, 2)}

def simulate_twap(df):
    start = df["ts_event"].min()
    end = start + timedelta(seconds=60)
    interval = timedelta(seconds=1)
    filled = 0
    cost = 0.0
    shares_per_second = ORDER_SIZE // 60

    current_time = start
    while filled < ORDER_SIZE and current_time <= end:
        snapshot = df[df["ts_event"] >= current_time].iloc[0]
        ask = snapshot["ask_px_00"]
        size = snapshot["ask_sz_00"]
        to_buy = min(size, shares_per_second, ORDER_SIZE - filled)
        cost += to_buy * ask
        filled += to_buy
        current_time += interval

    return {"total_cash": cost, "avg_fill_px": round(cost / filled, 2)}

def simulate_vwap(df):
    total_volume = df["ask_sz_00"].sum()
    filled = 0
    cost = 0.0
    for _, row in df.iterrows():
        ask = row["ask_px_00"]
        size = row["ask_sz_00"]
        allocation = int((size / total_volume) * ORDER_SIZE)
        to_buy = min(size, allocation, ORDER_SIZE - filled)
        cost += to_buy * ask
        filled += to_buy
        if filled >= ORDER_SIZE:
            break
    return {"total_cash": cost, "avg_fill_px": round(cost / filled, 2)}

# Run strategies
baselines = {
    "best_ask": simulate_best_ask(df),
    "twap": simulate_twap(df),
    "vwap": simulate_vwap(df)
}

# Save
with open("baselines.json", "w") as f:
    json.dump(baselines, f, indent=2)

print("✅ Baselines saved to baselines.json")
