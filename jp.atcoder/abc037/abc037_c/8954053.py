import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, k = I[:2]
a = I[2:]

def main():
    res = np.minimum(np.arange(1, n+1), np.arange(n, 0, -1))
    res = np.minimum(res, k)
    ans = np.sum(a * res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
