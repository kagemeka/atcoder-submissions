# 2019-11-18 00:38:19(JST)
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
    n, *p = [int(x) for x in sys.stdin.read().split()]

    ans = 0
    for l in range(n-1):
        if p[l] < p[l+1]:
            largest, second = p[l+1], p[l]
        else:
            largest, second = p[l], p[l+1]
        ans += second
        for r in range(l+2, n):
            if p[r] > largest:
                second, largest = largest, p[r]
            elif p[r] > second:
                second = p[r]
            ans += second
    print(ans)


if __name__ == "__main__":
    main()
