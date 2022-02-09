# 2019-11-15 00:35:39(JST)
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

def nCr(n, r):
    r = min(r, n - r)
    upper = reduce(op.mul, range(n, n-r, -1), 1)
    lower = reduce(op.mul, range(r, 0, -1), 1)
    return upper // lower

mod = 10 ** 9 + 7

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]

    for i in range(1, k+1):
        if i <= n - k + 1:
            print(nCr(n-k+1, i) * nCr(k-1, i-1) % mod)
        else:
            print(0) # k > n - k + 1 のとき、 i > n - k - 1 となる並べ方は存在しない

if __name__ == "__main__":
    main()
