import sys
import numpy as np

ab = np.array(sys.stdin.read().split(), dtype=np.int64)
n, ab = ab[0], ab[1:].reshape(-1, 2)

def main():
    res = np.zeros(10 ** 6 + 2, dtype=np.int64)
    np.add.at(res, ab[:, 0], 1)
    np.subtract.at(res, ab[:, 1]+1, 1)
    res = np.cumsum(res)
    print(np.amax(res))

if __name__ ==  '__main__':
    main()
