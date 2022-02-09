import sys
import numpy as np

MOD = 10 ** 9 + 7

n, *a = map(int, sys.stdin.read().split())
a = np.array(a, dtype=np.int64)

def main():
    s = 0
    for i in range(n-1):
        s += np.sum(a[i] ^ a[i+1:]) % MOD
        s %= MOD
    return s

if __name__ == '__main__':
    ans = main()
    print(ans)
