# 2019-11-20 12:21:36(JST)
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
    s = sys.stdin.readline().rstrip()

    count = 0
    for i in range(len(s)-1):
        if s[i+1] != s[i]:
            count+= 1

    print(count)


if __name__ == "__main__":
    main()
