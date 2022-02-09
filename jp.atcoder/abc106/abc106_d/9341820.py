import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m, q = I[:3]
l, r = I[3:3+m*2].reshape(-1, 2).T
p, q = I[3+m*2:].reshape(-1, 2).T

def main():
    res = np.zeros((n+2, n+2), dtype=np.int64)

    np.add.at(res, (np.full(m, 1), r), 1)
    np.add.at(res, (l+1, r), -1)
    np.add.at(res, (np.full(m, 1), np.full(m, n+1)), -1)
    np.add.at(res, (l+1, np.full(m, n+1)), 1)
    res = np.cumsum(res, axis=0)
    res = np.cumsum(res, axis=1)

    ans = res[p, q]
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
