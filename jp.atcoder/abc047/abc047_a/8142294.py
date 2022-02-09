# 書き方を少し変えたver

packs = [int(candies) for candies in input().split()]
N = int(len(packs))
if sum(packs) % 2 == 0:
    half = int(sum(packs) / 2)
else:
    print('No')
    exit()

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
