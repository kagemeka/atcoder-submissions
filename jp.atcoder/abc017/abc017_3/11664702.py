import sys
import numpy as np

n, m = map(int, sys.stdin.readline().split())
l, r, s = np.array(sys.stdin.read().split(), dtype=np.int32).reshape(-1, 3).T
def main():
    res = np.zeros(m + 1, dtype=np.int32)
    np.add.at(res, l - 1, s)
    np.subtract.at(res, r, s)
    np.cumsum(res, out=res)
    print(s.sum() - np.amin(res[:-1]))

if __name__ ==  '__main__':
    main()
