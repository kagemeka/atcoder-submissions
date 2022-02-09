import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
d = np.array([sys.stdin.readline().split() for _ in range(n)], dtype=np.int64)
p = np.array(sys.stdin.read().split(), dtype=np.int64)[1:]

d = np.pad(d, 1)
d = np.cumsum(d, axis=0)
d = np.cumsum(d, axis=1)

def main():
    ma = np.zeros((n + 1, n + 1), dtype=np.int64)
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            res = d[y:n+1, x:n+1] - d[0:n-y+1, x:n+1] - d[y:n+1, 0:n-x+1] + d[0:n-y+1, 0:n-x+1]
            ma[y][x] = np.amax(res)

    res = np.arange(n ** 2 + 1)[:, None]
    i = np.arange(1, n + 1)
    res = ma[i, np.minimum(res // i, n)]
    res = np.amax(res, axis=1)
    print(*res[p], sep='\n')

if __name__ == '__main__':
    main()
