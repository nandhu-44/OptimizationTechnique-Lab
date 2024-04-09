import numpy as np
from collections import defaultdict

def vogel_approximation_method(cost_matrix, supply, demand):
    m, n = cost_matrix.shape
    supply = defaultdict(int, dict(enumerate(supply)))
    demand = defaultdict(int, dict(enumerate(demand)))

    # Initialize allocation and total cost
    allocation = defaultdict(lambda: defaultdict(int))
    total_cost = 0

    # Create dictionaries for penalty calculation
    row_penalties = {source: sorted(range(n), key=lambda dest: cost_matrix[source, dest]) for source in range(m)}
    col_penalties = {dest: sorted(range(m), key=lambda source: cost_matrix[source, dest]) for dest in range(n)}

    while supply and demand:
        # Calculate row and column penalties
        row_penalties_values = {}
        col_penalties_values = {}
        for source in supply:
            if len(row_penalties[source]) > 1:
                row_penalties_values[source] = cost_matrix[source, row_penalties[source][1]] - cost_matrix[source, row_penalties[source][0]]
            else:
                row_penalties_values[source] = cost_matrix[source, row_penalties[source][0]]

        for dest in demand:
            if len(col_penalties[dest]) > 1:
                col_penalties_values[dest] = cost_matrix[col_penalties[dest][1], dest] - cost_matrix[col_penalties[dest][0], dest]
            else:
                col_penalties_values[dest] = cost_matrix[col_penalties[dest][0], dest]

        # Find the maximum row and column penalties
        max_row_penalty = max(row_penalties_values.values()) if row_penalties_values else 0
        max_col_penalty = max(col_penalties_values.values()) if col_penalties_values else 0

        # Choose the source and destination based on the maximum penalty
        if max_row_penalty >= max_col_penalty:
            source = max(row_penalties_values, key=row_penalties_values.get)
            dest = row_penalties[source][0]
        else:
            dest = max(col_penalties_values, key=col_penalties_values.get)
            source = col_penalties[dest][0]

        # Allocate and update supply, demand, and total cost
        allocated_amount = min(supply[source], demand[dest])
        allocation[source][dest] += allocated_amount
        total_cost += cost_matrix[source, dest] * allocated_amount
        supply[source] -= allocated_amount
        demand[dest] -= allocated_amount

        # Remove exhausted sources and destinations from penalty dictionaries
        if supply[source] == 0:
            del supply[source]
            for dest_key in row_penalties[source]:
                col_penalties[dest_key].remove(source)

        if demand[dest] == 0:
            del demand[dest]
            for source_key in col_penalties[dest]:
                row_penalties[source_key].remove(dest)

    # return allocation, total_cost
    
    # Create an allocation matrix from the defaultdict
    allocation_matrix = np.zeros_like(cost_matrix, dtype=int)
    for source, dest_alloc in allocation.items():
        for dest, amount in dest_alloc.items():
            allocation_matrix[source, dest] = amount

    return allocation_matrix, total_cost

# Example usage:
cost_matrix = np.array([[3, 1, 7, 4], [2, 6, 5, 9], [8, 3, 3, 2]])
supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

allocation, total_cost = vogel_approximation_method(cost_matrix, supply, demand)

print("Vogel's Approximation Method Allocation Matrix:")
print(allocation)
print(f"Total Cost: {total_cost}")