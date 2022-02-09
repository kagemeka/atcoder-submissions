import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
R, C, K, n = I[:4]
r, c = I[4:].reshape(-1, 2).T
r -= 1; c -= 1
grid = np.zeros((R, C), dtype=np.int64)
grid[r, c] = 1

def main():
    y = np.sum(grid, axis=1)[:, None]
    x = np.sum(grid, axis=0)
    res = y + x
    res[grid == 1] -= 1
    ans = np.bincount(res.ravel())[K]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
