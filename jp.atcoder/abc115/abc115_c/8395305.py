# 2019-11-11 18:30:26(JST)
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
    n, k, *h = (int(x) for x in sys.stdin.read().split())
    h.sort()
    diffs = []
    for i in range(n - k + 1):
        diffs.append(h[i+k-1] - h[i])
    print(min(diffs))

if __name__ == "__main__":
    main()
