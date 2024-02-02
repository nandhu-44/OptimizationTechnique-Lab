from scipy.optimize import linprog

c = [-3, -2]
A = [
    [2, 1],
    [1, 1],
    [-1, 0],
    [0, -1]
]
b = [500, 400, -100, -50]
x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

optimal_chocolate_cakes = result.x[0]
optimal_vanilla_cakes = result.x[1]
max_revenue = -result.fun

print(f"Chocolate cakes: {optimal_chocolate_cakes:.2f} units")
print(f"Vanilla cakes: {optimal_vanilla_cakes:.2f} units")
print(f"Total revenue: ${max_revenue:.2f}")
