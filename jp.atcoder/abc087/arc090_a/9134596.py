import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
l1, l2 = I[1:].reshape(2, n)

def main():
    res = 0
    for i in range(n):
        res = max(res, np.sum(l1[:i+1]) + np.sum(l2[i:]))
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
