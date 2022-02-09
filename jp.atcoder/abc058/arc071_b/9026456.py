import sys
import numpy as np

MOD = 10 ** 9 + 7

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
x = I[2:2+n]
y = I[2+n:]

def main():

    sdx = np.sum(x * np.arange(n) - x * np.arange(n-1, -1, -1)) % MOD
    sdy = np.sum(y * np.arange(m) - y * np.arange(m-1, -1, -1)) % MOD
    ans = sdx * sdy % MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
