# 2019-11-20 14:30:57(JST)
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
    s = '0' + sys.stdin.readline().rstrip() # s[r-1:l-1:-1]でのバグを防ぐため
    n = int(sys.stdin.readline().rstrip())
    lr = [tuple(int(x) for x in sys.stdin.readline().split()) for _ in range(n)]

    for i in range(n):
        l, r = lr[i][0], lr[i][1]+1
        s = s[:l] + s[r-1:l-1:-1] + s[r:]

    print(s[1:])


if __name__ == "__main__":
    main()
