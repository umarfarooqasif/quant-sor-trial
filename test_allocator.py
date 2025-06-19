from allocator import allocate, Venue

venues = [
    Venue(ask=49.90, ask_size=1500, fee=0.01, rebate=0.002),
    Venue(ask=49.95, ask_size=2000, fee=0.01, rebate=0.002),
    Venue(ask=49.88, ask_size=2500, fee=0.01, rebate=0.002)
]

best_split, best_cost = allocate(
    order_size=5000,
    venues=venues,
    lambda_over=0.4,
    lambda_under=0.6,
    theta=0.3
)

print("✅ Best Split:", best_split)
print("💰 Expected Cost:", best_cost)
