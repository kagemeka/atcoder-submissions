import sys
import numpy as np

n, k = map(int, sys.stdin.readline().split())
h = np.array(sys.stdin.read().split(), dtype=np.int64)
h.sort()

def main():
    res = np.amin(h[k-1:] - h[:-k+1])
    print(res)

if __name__ ==  '__main__':
    main()
