import sys

*I, = map(int, sys.stdin.read().split())
n, m, Q = I[:3]
lr = zip(*[iter(I[3:3+m*2])] * 2)
pq = zip(*[iter(I[3+m*2:])] * 2)

def main():
    res = [[0] * (n + 2) for _ in range(n+2)]

    for l, r in lr:
        res[1][r] += 1
        res[1][n+1] -= 1
        res[l+1][r] -= 1
        res[l+1][n+1] += 1

    for i in range(1, n+2):
        for j in range(1, n+1):
            res[i][j+1] += res[i][j]

    for j in range(1, n+2):
        for i in range(1, n+1):
            res[i+1][j] += res[i][j]

    for p, q in pq:
        yield res[p][q]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
