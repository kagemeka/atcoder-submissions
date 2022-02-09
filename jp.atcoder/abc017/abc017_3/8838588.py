import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
l, r, s = I[2:].reshape(-1, 3).T

def main():
    total = np.sum(s)
    res = np.zeros(m+2, np.int64)
    np.add.at(res, l, s)
    np.subtract.at(res, r+1, s)
    res = np.cumsum(res)
    ans = np.amax(total - res[1:-1])
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
