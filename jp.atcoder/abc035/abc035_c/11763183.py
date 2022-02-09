import sys
import numpy as np

n, q, *lr = map(int, sys.stdin.read().split())
l, r = np.array(lr).reshape(q, 2).T
l -= 1; r -= 1

def main():
    res = np.zeros(n + 1, dtype=np.int32)
    np.add.at(res, l, 1)
    np.subtract.at(res, r + 1, 1)
    np.cumsum(res, out=res)
    print(''.join((res[:-1] & 1).astype(str)))

if __name__ == '__main__':
    main()
