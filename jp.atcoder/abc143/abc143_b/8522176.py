# 2019-11-19 10:28:31(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np


def main():
    n, *d = map(int, sys.stdin.read().split())

    total = 0
    for i, j in itertools.combinations(d, 2):
        total += i * j
    print(total)


if __name__ == "__main__":
    main()
