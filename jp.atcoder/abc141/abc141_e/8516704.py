# 2019-11-18 17:34:23(JST)
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
    n, s = sys.stdin.read().split()
    n = int(n)

    ans = 0
    i, j = 0, 1
    while j < n:
        t = s[i:j]
        if t in s[j:]:
            ans = max(ans, j - i)
            j += 1
        else:
            i += 1
    print(ans)

if __name__ == "__main__":
    main()
