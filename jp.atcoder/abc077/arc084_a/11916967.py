import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a, b, c = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(3, n)
a.sort(); c.sort()

def main():
    print(np.sum(np.searchsorted(a, b) * (n - np.searchsorted(c, b, side='right'))))

if __name__ ==  '__main__':
    main()
