# 2019-11-19 01:10:02(JST)
import sys
import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
from scipy.misc import comb # (default: exact=False)
# import numpy as np

# def nCr(n, r):
#     r = min(n, r)
#     return np.cumprod(range(n, n-r, -1)) // np.cumprod(range(r, 0, -1))

def main():
    n, *a = [int(x) for x in sys.stdin.read().split()]
    s = list(itertools.accumulate(a))


    res = s.count(0)
    for x in [x for x in collections.Counter(s).values() if x >= 2]:
        res += comb(x, 2, exact=True)

    print(res)

if __name__ == "__main__":
    main()
