import sys

inf = float('inf')

n, m, x = map(int, sys.stdin.readline().split())
C = []
A = []
for _ in range(n):
    c, *a = map(int, sys.stdin.readline().split())
    C.append(c)
    A.append(a)

def main():
    ans = inf
    for i in range(1 << n):
        res = [0] * m
        cost = 0
        for j in range(n):
            if i >> j & 1:
                cost += C[j]
                for k in range(m):
                    res[k] += A[j][k]
        for r in res:
            if r < x: break
        else:
            ans = min(ans, cost)
    if ans == inf:
        print(-1)
    else:
        print(ans)





if __name__ == '__main__':
    main()
