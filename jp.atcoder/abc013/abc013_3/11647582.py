import sys
import numpy as np

n, h, a, b, c, d, e = map(int, sys.stdin.read().split())

def main():
    x = np.arange(n + 1, dtype=np.int64)
    y = (e * (n - x) - h - b * x) // (d + e) + 1
    np.maximum(y, 0, out=y)
    np.minimum(y, n - x, out=y)
    print(np.amin(a * x + c * y))

if __name__ ==  '__main__':
    main()
