import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.float)
n = int(I[0])

def main():
    h, s = I[1:].reshape(-1, 2).T
    h += s * n
    res = np.zeros(n)
    for _ in range(n):
        h -= s
        i = np.argmin(h)
        res[i] = h[i]
        h[i] = np.inf

    ans = np.amax(res)
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)

# TLE解法
