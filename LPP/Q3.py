from scipy.optimize import linprog

c = [-20, -30]
A = [
    [1, 5],
    [3, 1]
]
b = [125, 80]
x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

optimal_chairs = result.x[0]
optimal_tables = result.x[1]
max_profit = -result.fun

print(f"Chairs: {optimal_chairs:.2f} units")
print(f"Tables: {optimal_tables:.2f} units")
print(f"Total profit: ${max_profit:.2f}")
