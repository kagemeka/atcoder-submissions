import sys
import numpy as np

h, w, k, n, *rc = map(int, sys.stdin.read().split())
r, c = np.array(rc, dtype=np.int32).reshape(n, 2).T - 1

def main():
    y = np.bincount(r, minlength=h).astype(np.int32)
    x = np.bincount(c, minlength=w).astype(np.int32)
    cy = np.bincount(y, minlength=k+1)
    cx = np.bincount(x, minlength=k+1)
    res = np.sum(cy[:k+1] * cx[k::-1])
    real = np.bincount(y[r] + x[c] - 1, minlength=k+1)
    res += real[k] - real[k-1]
    print(res)

if __name__ ==  '__main__':
    main()
