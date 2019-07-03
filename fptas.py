import numpy as np

def generate_instance(capacity=14, volume=None, n_obj=4):
    profits = [16, 22, 12, 8]
    weights = [5, 7, 4, 3]
    return profits, weights

def base_capacity(p, w, s):
    if s < w:
        return 0
    return p

def base_profit(p, w, s):
    if s == p:
        return w
    if s == 0:
        return 0
    return np.inf

def solve_instance(capacity, volume, profits, weights, base=base_capacity):
    n = len(profits)
    S = capacity+1
    table = [[0]*S]*n  #dim: n,b
    table = np.array(table)
    print(f'Shape of table: {table.shape}')
    
    for i in range(0, n):
        table[i, 0] = 0

    for s in range(0, S):
        table[n-1, s] = base(profits[n-1], weights[n-1], s)

    for i in range(n-2, -1, -1):
        for s in range(0, S):
            if s < weights[i]:
                table[i, s] = table[i+1, s]
            else:
                table[i, s] = max(table[i+1, s], profits[i]+table[i+1, s-weights[i]])

    return table