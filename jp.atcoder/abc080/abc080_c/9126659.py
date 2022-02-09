import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
f = I[1:1+10*n].reshape(n, 10)
p = I[1+10*n:].reshape(n, 11)

def main():
    schedules = np.arange(1, 2**10)[:, None] >> np.arange(10) & 1

    res = f & schedules[:, None]
    res = np.sum(res, axis=2)

    res = p[np.arange(n), res]
    res = np.sum(res, axis=1)

    ans = np.amax(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
