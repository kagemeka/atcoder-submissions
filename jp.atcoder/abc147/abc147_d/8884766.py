import sys
import numpy as np

MOD = 10 ** 9 + 7

n, *a = map(int, sys.stdin.read().split())
a = np.array(a, dtype=np.int64)

def main():
    ans = 0
    for i in range(60):
        b = (a >> i) & 1
        x = np.count_nonzero(b)
        y = n - x
        x *= y
        x *= pow(2, i, MOD)
        ans += x
    ans %= MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
