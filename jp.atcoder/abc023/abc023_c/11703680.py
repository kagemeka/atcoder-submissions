import sys
import numpy as np

h, w, k, n, *rc = map(int, sys.stdin.read().split())
r, c = np.array(rc, np.int32).reshape(n, 2).T - 1

def main():
    y = np.bincount(r, minlength=h+1)
    x = np.bincount(c, minlength=w+1)
    cy = np.bincount(y, minlength=k+1)
    cx = np.bincount(x, minlength=k+1)
    tmp = np.sum(cy[:k+1] * cx[k::-1])
    real = np.bincount(y[r] + x[c], minlength=k+2)
    res = tmp + real[k+1] - real[k]
    print(res)

if __name__ ==  '__main__':
    main()
