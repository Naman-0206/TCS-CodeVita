n = int(input())
ids = list(map(int, input().split()))
cost = list(map(int, input().split()))
money  = int(input())

id_cost = zip(ids, cost)

# max free quantity
# max free cost

id_cost = sorted(id_cost, key=lambda x: x[0], reverse=True)
freeqty = [0]*n
freecost = [0]*n

for i, (id, cost) in enumerate(id_cost):
    for j in range(0,i):
        if id_cost[j][0]%id == 0:
            freeqty[j] += 1
            freecost[j] += cost

id_cost_qty_fcost = []
for i, (id, cost) in enumerate(id_cost):
    id_cost_qty_fcost.append((cost, freeqty[i], freecost[i]))

# id_cost_qty_fcost = sorted(id_cost_qty_fcost, key=lambda x: x[1])
# id_cost_qty_fcost = sorted(id_cost_qty_fcost, key=lambda x: x[2], reverse=True)

# id_cost_qty_fcost = sorted(id_cost_qty_fcost, key=lambda x: x[2]/x[1], reverse=True)


# print(id_cost_qty_fcost)

def max_qty_max_cost(products, m):
    dp = [0] * (m + 1)
    free_cost = [0] * (m + 1)
    
    for cost, qty, fcost in products:
        for budget in range(cost, m + 1):
            new_free_qty = dp[budget - cost] + qty
            new_free_cost = free_cost[budget - cost] + fcost
            
            if new_free_qty > dp[budget]:
                dp[budget] = new_free_qty
                free_cost[budget] = new_free_cost

            elif new_free_qty == dp[budget] and new_free_cost > free_cost[budget]:
                free_cost[budget] = new_free_cost
    
    return dp[m], free_cost[m]


max_qty, max_free_cost = max_qty_max_cost(id_cost_qty_fcost, money)
print(max_qty, max_free_cost, end="")
