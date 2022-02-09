# 2019-11-18 23:58:23(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np


def main():
    n, *l = [int(x) for x in sys.stdin.read().split()]
    l.sort()
    count = 0
    for i in range(n-2):
        a = l[i]
        for j in range(i+1, n-1):
            b = l[j]
            count += (bi_l(l, a + b) - 1) - j

    print(count)

if __name__ == "__main__":
    main()
