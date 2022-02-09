# 2019-11-19 19:43:48(JST)
import sys
# import collections
import math
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
    n = int(sys.stdin.readline().rstrip())

    dist = n
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            dist = min(dist, i + j - 2)
    print(dist)

if __name__ == "__main__":
    main()
