import sys
import numpy as np

grid = np.array(sys.stdin.read().split(), dtype=np.int8).reshape(3, 3)

def main():
    grid[:, :] -= grid[0]
    grid[:, :] -= grid[:, 0][:, None]
    print('No' if np.any(grid) else 'Yes')

if __name__ ==  '__main__':
    main()
