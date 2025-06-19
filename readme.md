# 🚀 Quant Developer Work Trial – Smart Order Router

## 📺 Video Walkthrough  
[Watch here](https://youtu.be/O7i47sieQBQ)

---

## 👤 Candidate Info
- **Name:** Umar Farooq  
- **GitHub:** [umarfarooqasif](https://github.com/umarfarooqasif)  
- **Project Repo:** [quant-sor-trial](https://github.com/umarfarooqasif/quant-sor-trial)

---

## 🎯 Objective

Build a Smart Order Router (SOR) using the Cont & Kukanov model, simulate market data using Kafka, backtest performance against baseline strategies, and deploy the complete pipeline on an AWS EC2 instance.

---

## 📂 Folder Structure

├── allocator.py  
├── backtest.py  
├── baseline_strategies.py  
├── finalize_results.py  
├── kafka_producer.py  
├── test_allocator.py  
├── docker-compose.yml  
├── requirements.txt  
├── output.json  
├── baselines.json  
├── final_result.json  
├── l1_day.csv (NOT uploaded)  
├── README.md  
└── __pycache__/  
---

## 🧠 Key Concepts

- **Kafka Producer:** Streams `l1_day.csv` line-by-line to Kafka topic `mock_l1_stream`.  
- **Kafka Consumer & Backtest:** Consumes stream and applies allocator logic to simulate order fills over time.  
- **Allocator:** Implements the static Cont-Kukanov model for optimal order distribution using cost penalties and queue risk.  
- **Parameter Tuning:** Grid search over `lambda_over`, `lambda_under`, and `theta_queue`.  
- **Benchmarking:** Compared against Best Ask, TWAP, and VWAP strategies.

---

## 🧪 Sample Output

```json
{
  "best_parameters": {
    "lambda_over": 0.4,
    "lambda_under": 0.6,
    "theta_queue": 0.3
  },
  "optimized": {
    "total_cash": 248750,
    "avg_fill_px": 49.75
  },
  "baselines": {
    "best_ask": {"total_cash": 250000, "avg_fill_px": 50.00},
    "twap": {"total_cash": 251000, "avg_fill_px": 50.20},
    "vwap": {"total_cash": 249800, "avg_fill_px": 49.96}
  },
  "savings_vs_baselines_bps": {
    "best_ask": 5.0,
    "twap": 15.0,
    "vwap": 4.2
  }
}

☁️ EC2 Deployment
Instance: t3.micro (Ubuntu 22.04)

SSH Access: Configured with sor-key.pem

Kafka & Zookeeper: Installed manually via shell

Docker Compose: Installed via official Docker script

🛠️ Run Commands
docker-compose up -d
python kafka_producer.py
python backtest.py

✅ Deliverables Recap
✅ allocator.py

✅ kafka_producer.py

✅ backtest.py

✅ output.json

✅ baselines.json

✅ final_result.json

✅ AWS EC2 deployment

✅ Public GitHub repository

✅ Final video walkthrough

🔗 Reference Links
📁 l1_day.csv – Market Snapshot Data(https://drive.google.com/file/d/1mmxHtT9L5vcTTbHay15piPeiDB2wm4mT/view)

📄 Cont-Kukanov Paper (https://arxiv.org/pdf/1210.1625)

🧠 Allocator Pseudocode (https://www.notion.so/Quant-Developer-Work-Trial-Blockhouse-210ca1a7e5b480d99a3cce6e0dc0992d?pvs=21)

🎥 Final Video showing:
EC2 login via SSH

Kafka producer streaming data

backtest.py running

Final JSON output with best parameters

Explanation of allocator logic and performance


