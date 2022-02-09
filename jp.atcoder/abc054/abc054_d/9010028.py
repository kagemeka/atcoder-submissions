import sys

INF = float('inf')

n, ma, mb = map(int, sys.stdin.readline().split())
abc = map(int, sys.stdin.read().split())
abc = list(zip(*[abc] * 3))

def main():
    sa = 0
    sb = 0
    for i in range(n):
        sa += abc[i][0]
        sb += abc[i][1]

    res = [[INF] * (sb + 1) for _ in range(sa + 1)]
    res[0][0] = 0

    for a, b, c in abc:

        for j in range(sa, -1, -1):
            for k in range(sb, -1, -1):
                if j >= a and k >= b:
                    res[j][k] = min(res[j][k], res[j-a][k-b] + c)

    ans = INF
    for i in range(1, min(sa//ma, sb//mb) + 1):
        ans = min(ans, res[ma*i][mb*i])

    if ans == INF:
        return -1
    else:
        return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
