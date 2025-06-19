import pandas as pd
import json
import time
from kafka import KafkaProducer
from datetime import datetime

# ---- CONFIG ----
CSV_PATH = 'l1_day.csv'  # make sure it's in the same folder
TOPIC = 'mock_l1_stream'
BROKER = 'localhost:9092'

# ---- LOAD CSV ----
df = pd.read_csv(CSV_PATH)

# Convert ts_event to datetime
df['ts_event'] = pd.to_datetime(df['ts_event'])

# Filter window: 13:36:32 to 13:45:14 UTC
start_time = pd.to_datetime('13:36:32').time()
end_time = pd.to_datetime('13:45:14').time()
df = df[df['ts_event'].dt.time.between(start_time, end_time)]

# ---- SETUP KAFKA PRODUCER ----
producer = KafkaProducer(
    bootstrap_servers=BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# ---- STREAM DATA TO KAFKA ----
prev_ts = None
for _, row in df.iterrows():
    ts = row['ts_event']
    
    # Calculate time delay
    if prev_ts is not None:
        delay = (ts - prev_ts).total_seconds()
        time.sleep(max(0, delay))  # simulate real-time
    prev_ts = ts

    # Prepare message
    message = {
        "timestamp": ts.isoformat(),
        "venue": row['publisher_id'],
        "ask": float(row['ask_px_00']),
        "ask_size": int(row['ask_sz_00'])
    }

    # Send to Kafka
    producer.send(TOPIC, value=message)
    print(f"[{ts}] Sent to Kafka → {message}")

producer.flush()
producer.close()
