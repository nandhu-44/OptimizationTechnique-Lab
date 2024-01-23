def knapsack(W, weights, profits, n):
    c = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            weight = weights[i - 1]
            if weight <= j:
                c[i][j] = max(c[i - 1][j], profits[i - 1] + c[i - 1][j - weight])
            else:
                c[i][j] = c[i - 1][j]

    print_items(c, weights, profits, n, W)

    return c[n][W]

def print_items(c, weights, profits, n, W):
    i, j = n, W
    result = []
    while i > 0 and j > 0:
        if c[i][j] != c[i - 1][j]:
            result.append(i)
            j -= weights[i - 1]
        i -= 1

    print("Items selected: [{}]".format(", ".join(map(str, result[::-1]))))

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    W = int(input("Enter the capacity of the knapsack: "))
    
    weights = list(map(int, input("Enter the weights of the items: ").split()))
    profits = list(map(int, input("Enter the profits of the items: ").split()))

    max_profit = knapsack(W, weights, profits, n)
    print("The maximum profit is:", max_profit)
