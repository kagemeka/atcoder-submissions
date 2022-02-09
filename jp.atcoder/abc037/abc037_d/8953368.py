import sys
from collections import OrderedDict
import numpy as np

MOD = 10 ** 9 + 7

I = np.array(sys.stdin.read().split(), dtype=np.int64)
h, w = I[:2]
grid = I[2:].reshape(h, w)
grid = np.pad(grid, 1, mode='constant')

def main():
    idx = OrderedDict()
    for i in range(1, h+1):
        for j in range(1, w+1):
            val = grid[i, j]
            if val in idx:
                idx[val].append((i, j))
            else:
                idx[val] = [(i, j)]

    res = np.zeros((h+2, w+2), dtype=np.int64)
    res[1:h+1, 1:w+1] = 1
    ans = 0
    for val, indices in sorted(idx.items()):
        for i, j in indices:
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                y = i + dy
                x = j + dx
                if grid[y, x] < grid[i, j]:
                    res[i, j] += res[y, x]
            res[i, j] %= MOD
            ans += res[i, j]
            ans %= MOD

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
