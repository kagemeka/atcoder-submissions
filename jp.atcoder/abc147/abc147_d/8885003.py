import sys
import numpy as np

MOD = 10 ** 9 + 7

n, *a = map(int, sys.stdin.read().split())
a = np.array(a, dtype=np.int64)

powmod = [None] * 100
powmod[0] = 1
for i in range(60):
    powmod[i+1] = powmod[i] * 2 % MOD

def main():
    b = a >> np.arange(60).reshape(-1, 1) & 1
    x = np.count_nonzero(b, axis=1)
    y = n - x
    x *= y
    x *= powmod[:60]
    x %= MOD
    ans = np.sum(x) % MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)