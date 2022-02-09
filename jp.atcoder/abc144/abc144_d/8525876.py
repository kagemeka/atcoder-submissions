# 2019-11-19 19:43:48(JST)
import sys
# import collections
from math import atan, pi
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
    a, b, v = map(int, sys.stdin.readline().split())

    if v / a >= a * b / 2:
        ans = atan(2 * (b - v / a ** 2) / a) * 180 / pi
    else:
        ans = atan(a ** 2 * b / (2 * v)) * 180 / pi

    print(ans)

if __name__ == "__main__":
    main()
