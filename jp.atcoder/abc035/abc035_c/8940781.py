import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, q = I[:2]
l, r = I[2:].reshape(-1, 2).T - 1

def main():
    res = np.zeros(n+1, dtype=np.int64)
    np.add.at(res, l, 1)
    np.subtract.at(res, r+1, 1)
    res = np.cumsum(res)
    ans = res[:-1] % 2
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='')
