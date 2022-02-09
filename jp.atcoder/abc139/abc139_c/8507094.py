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
    n, *h = [int(x) for x in sys.stdin.read().split()]

    step = 0
    prev_height = 0
    max_step = 0
    for i in range(n):
        if h[i] <= prev_height:
            step += 1
        else:
            max_step = max(max_step, step)
            step = 0
        prev_height = h[i]
    max_step = max(max_step, step)
    print(max_step)

if __name__ == "__main__":
    main()
