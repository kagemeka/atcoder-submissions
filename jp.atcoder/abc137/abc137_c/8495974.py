# 2019-11-16 14:51:41(JST)
import sys
import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r, insort_left as in_l
# import itertools
# from functools import reduce
# import operator as op
from scipy.special import comb # comb(n, r, exact=True)
# import numpy as np
# import heapq
# import array


def main():
    n = int(sys.stdin.readline().rstrip())

    sorted_letters = [''.join(sorted(sys.stdin.readline().rstrip())) for _ in range(n)]

    count = 0
    for c in collections.Counter(sorted_letters).values():
        if c >= 2:
            count += comb(c, 2, exact=True)

    print(count)


if __name__ == "__main__":
    main()
