# 2019-11-17 20:44:23(JST)
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
    a, b = [int(x) for x in sys.stdin.readline().split()]
    extend = a - 1

    total_sockets = 1
    strips_count = 0
    if b >= 2:
        more_needed = True
    else:
        more_needed = False

    while more_needed:
        strips_count += 1
        total_sockets += extend
        if total_sockets >= b:
            more_needed = False

    print(strips_count)


if __name__ == "__main__":
    main()
