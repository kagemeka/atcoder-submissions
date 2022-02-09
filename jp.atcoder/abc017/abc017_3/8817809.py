import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
lrs = I[2:].reshape(-1, 3).T

def main():
    res = np.zeros(m+2, np.int64)
    for i in range(n):
        res[lrs[0][i]] += lrs[2][i]
        res[lrs[1][i]+1] -= lrs[2][i]

    res = np.cumsum(res)
    return np.sum(lrs[2]) - np.amin(res[1:-1])

if __name__ == '__main__':
    ans = main()
    print(ans)
