import sys

MOD = 10 ** 9 + 7

s = sys.stdin.readline().rstrip()
l = len(s)

def main():
    dp = [[0] * 13 for _ in range(l+1)]
    dp[0][0] = 1
    for i in range(l):
        d = s[i]
        if d != '?':
            d = int(d)
            for j in range(13):
                dp[i+1][(j*10+d)%13] += dp[i][j]
        else:
            for k in range(10):
                for j in range(13):
                    dp[i+1][(j*10+k)%13] += dp[i][j]

        for j in range(13):
            dp[i+1][j] %= MOD

    return dp[l][5]

if __name__ == '__main__':
    ans = main()
    print(ans)
