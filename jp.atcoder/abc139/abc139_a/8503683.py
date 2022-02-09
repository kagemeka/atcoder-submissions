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
    s, t = sys.stdin.read().split()

    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
