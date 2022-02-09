n, W = [int(x) for x in input().split()]
weight = []
value = []
for i in range(n):
    wi, vi = [int(x) for x in input().split()]
    weight.append(wi)
    value.append(vi)

dp = [[0] * (W+1)] * (n+1)

for i in range(n):
    for w in range(W+1):
        if w >= weight[i]:
            dp[i+1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]

ans = dp[n][W]
print(ans)
