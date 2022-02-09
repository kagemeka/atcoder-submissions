import sys

n = int(sys.stdin.readline().rstrip())
d = [[0] * (n + 1)]
d += [[0] + [int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
p, *p = map(int, sys.stdin.read().split())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        d[i][j] += d[i][j-1]

for j in range(1, n + 1):
    for i in range(1, n + 1):
        d[i][j] += d[i-1][j]

def main():
    maximum = [[0] * (n + 1) for _ in range(n + 1)]

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            for i in range(y, n + 1):
                for j in range(x, n + 1):
                    deliciousness = d[i][j] - d[i-y][j] - d[i][j-x] + d[i-y][j-x]
                    maximum[y][x] = max(maximum[y][x], deliciousness)

    res = [0] * (n ** 2 + 1)
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            res[y*x] = max(res[y*x], maximum[y][x])

    for i in range(1, len(res)):
        res[i] = max(res[i], res[i-1])

    for x in p:
        print(res[x])

if __name__ == '__main__':
    main()
