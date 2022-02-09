import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m, q = I[:3]
l, r = I[3:3+m*2].reshape(-1, 2).T
p, q = I[3+m*2:].reshape(-1, 2).T

def main():
    res = np.zeros((n+2, n+2), dtype=np.int64)

    np.add.at(res, (1, r), 1)
    res[1, n+1] += -1 * m
    np.add.at(res, (l+1, r), -1)
    np.add.at(res, (l+1, n+1), 1)
    res = np.cumsum(res, axis=1)
    res = np.cumsum(res, axis=0)

    ans = res[p, q]
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
