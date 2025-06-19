from typing import List, Tuple

class Venue:
    def __init__(self, ask: float, ask_size: int, fee: float, rebate: float):
        self.ask = ask
        self.ask_size = ask_size
        self.fee = fee
        self.rebate = rebate

def compute_cost(split: List[int], venues: List[Venue], order_size: int, lambda_over: float, lambda_under: float, theta: float) -> float:
    executed = 0
    cash_spent = 0.0

    for i in range(len(venues)):
        exe = min(split[i], venues[i].ask_size)
        executed += exe
        cash_spent += exe * (venues[i].ask + venues[i].fee)
        maker_rebate = max(split[i] - exe, 0) * venues[i].rebate
        cash_spent -= maker_rebate

    underfill = max(order_size - executed, 0)
    overfill = max(executed - order_size, 0)
    risk_pen = theta * (underfill + overfill)
    cost_pen = lambda_under * underfill + lambda_over * overfill

    return cash_spent + risk_pen + cost_pen

def allocate(order_size: int, venues: List[Venue], lambda_over: float, lambda_under: float, theta: float) -> Tuple[List[int], float]:
    step = 100
    splits = [[]]

    for v in range(len(venues)):
        new_splits = []
        for alloc in splits:
            used = sum(alloc)
            max_v = min(order_size - used, venues[v].ask_size)
            for q in range(0, max_v + 1, step):
                new_splits.append(alloc + [q])
        splits = new_splits

    best_cost = float('inf')
    best_split = []

    for alloc in splits:
        if sum(alloc) != order_size:
            continue
        cost = compute_cost(alloc, venues, order_size, lambda_over, lambda_under, theta)
        if cost < best_cost:
            best_cost = cost
            best_split = alloc

    return best_split, best_cost
