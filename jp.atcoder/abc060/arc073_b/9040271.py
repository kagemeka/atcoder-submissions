import sys

n, W = map(int, sys.stdin.readline().split())
wv = map(int, sys.stdin.read().split())

wv = sorted(zip(*[wv] * 2))
min_w = wv[0][0]
W2 = 4 * n

def main():
    dp = [[[0] * (W2 + 1) for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n):
        w, v = wv[i]
        w -= min_w - 1
        for j in range(1, i+2):
            for k in range(W2 + 1):
                if k + (min_w - 1) * j > W:
                    break
                dp[i+1][j][k] = dp[i][j][k]
                if k >= w:
                    dp[i+1][j][k] = max(dp[i][j][k], dp[i][j-1][k-w] + v)

    res = 0
    for j in dp[n]:
        res = max(res, max(j))

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
