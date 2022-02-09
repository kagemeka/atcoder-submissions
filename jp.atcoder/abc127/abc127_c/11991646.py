import sys
import numpy as np

n, m, *lr = map(int, sys.stdin.read().split())
l, r = np.array(lr).reshape(-1, 2).T

def main():
    res = max(0, r.min() - l.max() + 1)
    print(res)

if __name__ ==  '__main__':
    main()
