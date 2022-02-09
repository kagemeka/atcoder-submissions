import sys

n, a, *x = map(int, sys.stdin.read().split())

def main():
    res = [[[0] * (a * n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    res[0][0][0] = 1
    for i in range(n):
        cur = x[i]
        for j in range(i+2):
            for k in range(a * (i+1) + 1):
                res[i+1][j][k] += res[i][j][k]
                if k >= cur:
                    res[i+1][j][k] += res[i][j-1][k-cur]

    ans = 0
    for j in range(1, n+1):
        ans += res[n][j][j*a]

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
