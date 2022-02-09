import sys

n, k = map(int, sys.stdin.read().split())

def main():
    m = str(n)
    l = len(str(n))
    dp1 = [[0] * (k + 1) for _ in range(l+1)]
    dp2 = [[0] * (k + 1) for _ in range(l+1)]
    dp2[0][0] = 1
    for i in range(l):
        d = int(m[i])
        for j in range(k+1):
            dp1[i+1][j] += dp1[i][j]
            if d > 0:
                dp1[i+1][j] += dp2[i][j]
            if j >= 1:
                dp1[i+1][j] += dp1[i][j-1] * 9 + dp2[i][j-1] * max(d - 1, 0)

            if d == 0:
                dp2[i+1][j] += dp2[i][j]
            elif j >= 1:
                dp2[i+1][j] += dp2[i][j-1]

    return dp1[l][k] + dp2[l][k]

if __name__ == '__main__':
    ans = main()
    print(ans)
