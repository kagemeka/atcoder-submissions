import sys
import numpy as np
from scipy.optimize import brenth, bisect

I = np.array(sys.stdin.read().split(), dtype=np.float64)
n, k = I[:2].astype(np.int64)
water, percent = I[2:].reshape(-1, 2).T

def can_make(p):
    solt = water * (percent - p) / 100
    solt = np.sort(solt)[::-1]
    res = np.sum(solt[:k])
    return res

def main():
    ans = bisect(can_make, a=0, b=100)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
