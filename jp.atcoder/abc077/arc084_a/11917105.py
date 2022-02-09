import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a, b, c = np.sort(np.array(sys.stdin.read().split(), dtype=np.int64).reshape(3, n), axis=1)

def main():
    combs = np.sum(np.searchsorted(a, b) * (n - np.searchsorted(c, b, side='right')))
    print(combs)

if __name__ ==  '__main__':
    main()
