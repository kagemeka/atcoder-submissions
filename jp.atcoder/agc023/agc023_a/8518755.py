# 2019-11-19 01:10:02(JST)
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
    n, *a = [int(x) for x in sys.stdin.read().split()]
    s = list(itertools.accumulate(a))

    count = s.count(0)
    for i in range(n-1):
        for j in range(i+1, n):
            if s[j] - s[i] == 0:
                count += 1

    print(count)

if __name__ == "__main__":
    main()
