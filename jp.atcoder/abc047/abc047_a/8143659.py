packs = [int(candies) for candies in input().split()]
N = int(len(packs))
X = 2
if sum(packs) % X == 0:
    A = int(sum(packs) / X)
else:
    print('No')
    exit()

dp = [[False] * (A + 1)] * (N + 1)
dp[0][0] = True

for i in range(N):
    for j in range(A+1):
        if dp[i][j]:
            dp[i+1][j] = dp[i][j]
        elif j >= packs[i]:
            dp[i+1][j] = dp[i][j - packs[i]]

if dp[N][A]:
    ans = "Yes"
else:
    ans = "No"

print(ans)
