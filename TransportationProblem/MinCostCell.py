import numpy as np

def calculate_total_cost(allocation, cost_matrix):
    return np.sum(allocation * cost_matrix)

def minimum_cost_cell_method(cost_matrix, demand, supply):
    # Convert cost_matrix to float type and keep a copy of the original
    original_cost_matrix = cost_matrix.copy()
    cost_matrix = cost_matrix.astype(float)

    # Initialize allocation matrix
    allocation = np.zeros(cost_matrix.shape)

    # While there is still supply and demand
    while np.sum(demand) > 0 and np.sum(supply) > 0:
        # Find the cell with the minimum cost
        min_cost_index = np.unravel_index(np.argmin(cost_matrix, axis=None), cost_matrix.shape)

        # Allocate as much as possible to this cell
        allocation[min_cost_index] = min(demand[min_cost_index[1]], supply[min_cost_index[0]])

        # Update the supply and demand
        demand[min_cost_index[1]] -= allocation[min_cost_index]
        supply[min_cost_index[0]] -= allocation[min_cost_index]

        # Set the cost of this cell to infinity so it won't be chosen again
        cost_matrix[min_cost_index] = np.inf

    # Calculate the total cost using the original cost matrix
    total_cost = calculate_total_cost(allocation, original_cost_matrix)
    return allocation, total_cost

# Example usage:
cost_matrix = np.array([[3, 1, 7, 4], [2, 6, 5, 9], [8, 3, 3, 2]])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

allocation, total_cost = minimum_cost_cell_method(cost_matrix, demand, supply)
print("Minimum Cost Cell Method Allocation:")
print(allocation)
print("Total Cost:", total_cost)