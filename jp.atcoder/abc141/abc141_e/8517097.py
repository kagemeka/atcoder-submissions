# 2019-11-18 17:34:23(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np


def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    res = 0
    l, r = 0, 1
    while r <= l + (n - l) // 2:
        t = s[l:r]
        if t in s[r:]:
            res = max(res, r - l)
            r += 1
        else:
            l += 1
            if l == r:
                r += 1
    print(res)

if __name__ == "__main__":
    main()

# しゃくとり法的なやつ
