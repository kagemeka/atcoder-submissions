# 2019-11-16 21:01:15(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
from functools import reduce
import operator as op
# from scipy.misc import comb # float
# import numpy as np


mod = 10 ** 9 + 7

def comb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def main():
    x, y = [int(x) for x in sys.stdin.readline().split()]
    # n(+1, +2), m(+2, +1)
    n, m = (2 * y - x) / 3, (2 * x - y) / 3

    if n != abs(int(n)) or m != abs(int(m)):
        print(0)
        sys.exit()
    else:
        n, m = int(n), int(m)
        ans = comb(n+m, n) % mod
        print(ans)

if __name__ == "__main__":
    main()
