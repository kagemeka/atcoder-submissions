# 2019-11-16 14:51:41(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left as bi_l, bisect_right as bi_r, insort_left as in_l
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np
# import heapq
# import array


def main():
    n = int(sys.stdin.readline().rstrip())

    sorted_letters = []
    count = 0
    for _ in range(n):
        s = ''.join(sorted(sys.stdin.readline().rstrip()))
        count += bi_r(sorted_letters, s) - bi_l(sorted_letters, s)
        in_l(sorted_letters, s)
    print(count)

if __name__ == "__main__":
    main()
