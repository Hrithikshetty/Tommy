def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))

profit = [60, 100, 120]
weight = [10, 20, 30]
n = len(profit)
W = 10
print(knapSack(W, weight, profit, n))



























def knapsack_max_profit(weights, costs, capacity):
    num_items = len(weights)
    table = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(costs[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    selected_items = []
    total_weight = capacity

    for i in range(num_items, 0, -1):
        if table[i][total_weight] != table[i - 1][total_weight]:
            selected_items.append(i - 1)
            total_weight -= weights[i - 1]

    return table[num_items][capacity], selected_items

weights = [2, 3, 4, 5]
costs = [10, 20, 30, 40]
capacity = 10

max_profit, selected_items = knapsack_max_profit(weights, costs, capacity)
print("Maximum Profit:", max_profit)
print("Selected Coffee Beans (index):", selected_items)
print("Selected Coffee Beans (weight):", [weights[i] for i in selected_items])
print("Selected Coffee Beans (cost):", [costs[i] for i in selected_items])
