# 2019-11-18 00:38:19(JST)
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
    n = int(sys.stdin.readline().rstrip())

    eating_order = [int(x) for x in sys.stdin.readline().split()]
    base_point = sum([int(x) for x in sys.stdin.readline().split()])
    bonus_points = [0] + [int(x) for x in sys.stdin.readline().split()]

    total = base_point
    for i in range(n-1):
        if eating_order[i+1] == eating_order[i] + 1:
            total += bonus_points[eating_order[i]]

    print(total)

if __name__ == "__main__":
    main()
