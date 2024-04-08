import numpy as np


def calculate_total_cost(allocation, cost_matrix):
    return np.sum(allocation * cost_matrix)


def northwest_corner_method(cost_matrix, supply, demand):
    num_supply = len(supply)
    num_demand = len(demand)

    allocation = np.zeros((num_supply, num_demand))

    i, j = 0, 0
    while i < num_supply and j < num_demand:
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


# Example usage:
cost_matrix = np.array([[3, 1, 7, 4], [2, 6, 5, 9], [8, 3, 3, 2]])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

nw_allocation, nw_cost = northwest_corner_method(cost_matrix, supply, demand)
print("Northwest Corner Method Allocation:")
print(nw_allocation)
print("Total Cost:", nw_cost)
