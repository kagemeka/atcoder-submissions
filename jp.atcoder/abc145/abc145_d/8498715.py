# 2019-11-16 21:01:15(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
from scipy.misc import comb # float
# import numpy as np


mod = 10 ** 9 + 7

def main():
    x, y = [int(x) for x in sys.stdin.readline().split()]
    # n(+1, +2), m(+2, +1)
    n, m = (2 * y - x) / 3, (2 * x - y) / 3

    if n != abs(int(n)) or m != abs(int(m)):
        print(0)
        sys.exit()
    else:
        n, m = int(n), int(m)
        ans = comb(n+m, n, exact=True) % mod
        print(ans)

if __name__ == "__main__":
    main()
