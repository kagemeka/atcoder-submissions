import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
f = I[1:10*n+1].reshape(n, 10)
p = I[10*n+1:].reshape(n, 11)

def main():
    combs = np.arange(1, 1 << 10)[:, None] >> np.arange(10) & 1
    res = (combs[:, None] & f).sum(axis=2)
    res = p[np.arange(n), res[:, None]].sum(axis=2)
    print(res.max())

if __name__ ==  '__main__':
    main()
