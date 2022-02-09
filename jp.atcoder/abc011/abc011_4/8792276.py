import sys
import math
from scipy.special import comb

n, d, x, y = map(int, sys.stdin.read().split())

def main(n, d, x, y):
    x, y = abs(x), abs(y)

    if x % d != 0:
        return 0
    if y % d != 0:
        return 0

    x, y = x // d, y // d

    q = x + y
    r = n - q
    if r < 0 or r & 1:
        return 0

    res = 0

    for i in range(r // 2 + 1):
        u = y + i
        d = i
        l = (r - 2 * i) // 2

        res += math.pow(1 / 4, n) * comb(n, u, exact=True) * comb(n - u, d, exact = True) * comb(n - u - d, l, exact=True)

    return res

if __name__ == '__main__':
    print(main(n, d, x, y))
