import sys
import numpy as np

def main():
    grid = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(3, 3)

    grid = grid - grid[0]
    grid = grid.T
    grid = grid - grid[0]
    if np.all(grid == 0):
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)

if __name__ == "__main__":
    main()
