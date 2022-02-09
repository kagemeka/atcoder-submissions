# 2019-11-20 22:09:02(JST)
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
    s, k = sys.stdin.read().split()
    k = int(k)
    n = len(s)
    if k > n:
        print(0)
        sys.exit()

    cand = set()
    for i in range(n-k+1): # prefix
        sub = s[i:i+k]
        cand.add(sub)

    print(len(cand))
if __name__ == "__main__":
    main()
