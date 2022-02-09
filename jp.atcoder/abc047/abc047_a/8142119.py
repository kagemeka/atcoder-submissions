# DPで解く

packs = [int(candies) for candies in input().split()]
N = int(len(packs))
half = int(sum(packs) / 2)

dp = [[False] * (half + 1)] * (N + 1)
dp[0][0] = True

for i in range(N):
    for j in range(half+1):
        if dp[i][j]:
            dp[i+1][j] = dp[i][j]
        elif j >= packs[i]:
            dp[i+1][j] = dp[i][j - packs[i]]

if dp[N][half]:
    ans = "Yes"
else:
    ans = "No"

print(ans)
