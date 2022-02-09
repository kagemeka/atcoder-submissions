# 2019-11-17 10:52:21(JST)
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
import numpy as np


def main():
    n, *a = map(int, sys.stdin.read().split())

    max_cump = np.cumprod(a)[-1]

    upper = max_cump
    lower = 0
    for i in range(n):
        lower += max_cump / a[i]
    ans = upper / lower
    print(ans)

if __name__ == "__main__":
    main()
