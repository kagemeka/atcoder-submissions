import sys

n, a, *x = map(int, sys.stdin.read().split())

def main():
    for i in range(n):
        x[i] -= a
    x.sort()

    res = [[0] * 99*n for _ in range(n+1)]
    # res[i][49*n]を中心とする。
    res[0][49*n] = 1
    for i in range(n):
        for j in range(99*n):
            res[i+1][j] += res[i][j]
            cur = x[i]
            if cur >= 0:
                if j >= cur:
                    res[i+1][j] += res[i][j-cur]
            else:
                if j - cur <= 99 * n - 1:
                    res[i+1][j] += res[i][j-cur]

    ans = res[n][49*n] - 1
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
