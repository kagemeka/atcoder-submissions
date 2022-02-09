# 2019-11-19 10:28:31(JST)
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
    a, b = map(int, sys.stdin.readline().split())
    print(max(0, a - b * 2))

if __name__ == "__main__":
    main()
