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
    min_diff = h[-1] - h[0] # default value
    for i in range(n - k + 1):
        heights = h[i:i+k]
        diff = heights[-1] - heights[0]
        min_diff = min(min_diff, diff)
    print(min_diff)



if __name__ == "__main__":
    main()
