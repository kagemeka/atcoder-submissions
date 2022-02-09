import sys
import numpy as np

MOD = 10 ** 9 + 7

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
x = I[2:2+n]
y = I[2+n:]

def main():
    sx = np.cumsum(x) % MOD
    sy = np.cumsum(y) % MOD

    sdx = np.sum((sx[n-1] - sx[:n-1]) - x[:n-1] * ((n-1) - np.arange(n-1))) % MOD
    sdy = np.sum((sy[m-1] - sy[:m-1]) - y[:m-1] * ((m-1) - np.arange(m-1))) % MOD

    ans = sdx * sdy % MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
