import sys
import numpy as np

n, m = map(int, sys.stdin.readline().split())
x = np.array(sys.stdin.readline().split(), dtype=np.int64)
x.sort()

def main():
    d = np.sort(x[1:] - x[:-1])[::-1]
    d = np.concatenate((np.array([0]), np.cumsum(d)))
    res = d[m-1] - d[min(n, m) - 1]
    print(res)

if __name__ ==  '__main__':
    main()
