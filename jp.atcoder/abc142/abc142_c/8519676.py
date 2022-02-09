# 2019-11-18 23:58:23(JST)
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
    n, *a = [int(x) for x in sys.stdin.read().split()]
    a = list(enumerate(a, 1))
    a.sort(key=lambda x: x[1])
    for i in a:
        print(i[0], end=' ')

if __name__ == "__main__":
    main()
