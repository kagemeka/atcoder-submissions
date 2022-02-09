import sys
import numpy as np
from scipy.ndimage import distance_transform_cdt

r, c, k = map(int, sys.stdin.readline().split())
grid = np.array([list(s) for s in sys.stdin.read().split()], dtype='U1')
grid = np.pad(grid, 1, 'constant')
grid = (grid == 'o').astype(np.int16)

def main():
    res = distance_transform_cdt(grid, metric='taxicab')
    # The minimum of Manhattan distances from surrounding 'x'.
    print(np.count_nonzero(res >= k))

if __name__ == '__main__':
    main()
