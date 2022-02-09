import sys
import numpy as np

h, w = map(int, sys.stdin.readline().split())
grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(h)], dtype='U')
grid = np.pad(grid, 1, mode='constant')

def main():
    cnt = np.zeros((h+2, w+2))
    cnt[grid == '.'] = np.inf

    l = cnt.copy()
    r = cnt.copy()
    u = cnt.copy()
    d = cnt.copy()

    for i in range(1, w+1):
        l[1:h+1, i] = np.minimum(l[1:h+1, i], l[1:h+1, i-1]+1)
        i = w + 1 - i
        r[1:h+1, i] = np.minimum(r[1:h+1, i], r[1:h+1, i+1]+1)

    for i in range(1, h+1):
        u[i, 1:w+1] = np.minimum(r[i, 1:w+1], u[i-1, 1:w+1]+1)
        i = h + 1 - i
        d[i, 1:w+1] = np.minimum(d[i, 1:w+1], d[i+1, 1:w+1]+1)

    res = np.maximum(l + r + u + d - 3, 0).astype(np.int64)
    return np.amax(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
