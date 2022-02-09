import sys
import numpy as np

R, C, K = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline().rstrip())
r, c = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 2).T - 1
grid = np.zeros((R, C), dtype=np.int64)
grid[r, c] = 1

def main():
    res = np.sum(grid, axis=1).reshape(-1, 1) + np.sum(grid, axis=0)
    res[grid == 1] -= 1
    ans = np.count_nonzero(res == K)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
