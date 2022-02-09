# 2019-11-14 10:01:24(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, *w = [int(x) for x in sys.stdin.read().split()]

    min_diff = sum(w)
    for i in range(0, n-1):
        diff = abs(sum(w[:i+1]) - sum(w[i+1:]))
        min_diff = min(min_diff, diff)
    print(min_diff)

if __name__ == "__main__":
    main()
