import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
a, b = I[1:].reshape(2, n)

def main(a, b):
    a = a[:, None] >> np.arange(30) & 1
    # a = a.sum(axis=0)
    b = b[:, None] >> np.arange(30) & 1
    # b = b.sum(axis=0)

    res = a[:, None] + b
    for i in range(29):
        res[:, :, i+1] += res[:, :, i] // 2
        res[:, :, i] %= 2
    res = res.sum(axis=1).sum(axis=0) & 1
    ans = np.sum(2 ** np.arange(30) * res)
    return ans

if __name__ == '__main__':
    ans = main(a, b)
    print(ans)
