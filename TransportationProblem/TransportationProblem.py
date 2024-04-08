"""
Implement three methods to find basic feasible solutions in transportation problem

North West corner cell method
Minimum cost cell method
Vogels approximation method
"""

import numpy as np

def calculate_total_cost(allocation, cost_matrix):
    return np.sum(allocation * cost_matrix)

def northwest_corner_method(cost_matrix, supply, demand):
    rows, cols = len(supply), len(demand)
    allocation = np.zeros((rows, cols))

    i, j = 0, 0
    while i < rows and j < cols:
        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1

    total_cost = calculate_total_cost(allocation, cost_matrix)
    return allocation, total_cost

def minimum_cost_cell_method(cost_matrix, supply, demand):
    rows, cols = len(supply), len(demand)
    allocation = np.zeros((rows, cols))

    while np.sum(allocation) < np.sum(cost_matrix != 0):
        min_cost = float('inf')
        min_i, min_j = -1, -1

        for i in range(rows):
            for j in range(cols):
                if cost_matrix[i, j] < min_cost and supply[i] > 0 and demand[j] > 0:
                    min_cost = cost_matrix[i, j]
                    min_i, min_j = i, j
                    print("Min Cost:", min_cost, "Min i:", min_i, "Min j:", min_j)

        quantity = min(supply[min_i], demand[min_j])
        allocation[min_i, min_j] = quantity
        supply[min_i] -= quantity
        demand[min_j] -= quantity

    total_cost = calculate_total_cost(allocation, cost_matrix)
    return allocation, total_cost

def vogels_approximation_method(cost_matrix, supply, demand):
    rows, cols = len(supply), len(demand)
    allocation = np.zeros((rows, cols))

    while np.sum(allocation) < np.sum(cost_matrix != 0):
        penalties_row = [min(filter(lambda x: x > 0, cost_matrix[i])) for i in range(rows)]
        penalties_col = [min(filter(lambda x: x > 0, cost_matrix[:, j])) for j in range(cols)]

        max_penalty_row = max(penalties_row)
        max_penalty_col = max(penalties_col)

        if max_penalty_row >= max_penalty_col:
            i = penalties_row.index(max_penalty_row)
            j = np.argmin(cost_matrix[i])
        else:
            j = penalties_col.index(max_penalty_col)
            i = np.argmin(cost_matrix[:, j])

        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

    total_cost = calculate_total_cost(allocation, cost_matrix)
    return allocation, total_cost

cost_matrix = np.array([
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8, 3, 3, 2]
])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

nw_allocation, nw_cost = northwest_corner_method(cost_matrix, supply.copy(), demand.copy())
min_cost_allocation, min_cost = minimum_cost_cell_method(cost_matrix, supply.copy(), demand.copy())
vogel_allocation, vogel_cost = vogels_approximation_method(cost_matrix, supply.copy(), demand.copy())

print("Northwest Corner Method Allocation:")
print(nw_allocation)
print("Total Cost:", nw_cost)
print("\nMinimum Cost Cell Method Allocation:")
print(min_cost_allocation)
print("Total Cost:", min_cost)
print("\nVogel's Approximation Method Allocation:")
print(vogel_allocation)
print("Total Cost:", vogel_cost)
