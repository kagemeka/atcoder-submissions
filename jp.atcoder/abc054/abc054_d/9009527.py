import sys

INF = float('inf')

n, ma, mb = map(int, sys.stdin.readline().split())
a, b, c = [], [], []
for _ in range(n):
    ai, bi, ci = map(int, sys.stdin.readline().split())
    a.append(ai); b.append(bi); c.append(ci)

def main():
    sa = sum(a)
    sb = sum(b)
    res = [[[INF] * (sb + 1) for _ in range(sa + 1)] for _ in range(n + 1)]
    res[0][0][0] = 0
    for i in range(n):
        for j in range(sa + 1):
            for k in range(sb + 1):
                if j >= a[i] and k >= b[i]:
                    res[i+1][j][k] = min(res[i][j-a[i]][k-b[i]] + c[i], res[i][j][k])
                else:
                    res[i+1][j][k] = res[i][j][k]
    ans = INF
    for i in range(1, min(sa//ma, sb//mb)+1):
        ans = min(ans, res[n][ma * i][mb * i])

    if ans == INF:
        return -1
    else:
        return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
