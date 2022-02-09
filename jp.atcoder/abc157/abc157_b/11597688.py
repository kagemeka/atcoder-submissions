import sys
import numpy as np

a = np.array([sys.stdin.readline().split() for _ in range(3)], dtype=np.int64)
n = int(sys.stdin.readline().rstrip())
b = np.array(sys.stdin.read().split(), dtype=np.int64)
def main():
    c = np.isin(a, b)
    bl1 = np.any(np.all(c, axis=1))
    bl2 = np.any(np.all(c, axis=0))
    bl3 = np.all(np.diagonal(c))
    bl4 = np.all(np.diagonal(np.fliplr(c)))
    bl = bl1 | bl2 | bl3 | bl4
    print('Yes' if bl else 'No')

if __name__ ==  '__main__':
    main()
