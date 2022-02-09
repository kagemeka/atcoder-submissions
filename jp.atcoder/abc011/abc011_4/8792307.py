import sys
import math
from scipy.misc import comb

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
    P = math.pow(1 / 2, n)
    for i in range(r // 2 + 1):
        u = y + i
        d = i
        l = (r - 2 * i) // 2

        res += P * comb(n, u, exact=True) * comb(n - u, d, exact = True) * comb(n - u - d, l, exact=True) * P

    return res

if __name__ == '__main__':
    print(main(n, d, x, y))
