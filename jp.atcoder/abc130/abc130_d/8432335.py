# 2019-11-14 17:27:23(JST)
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
    n, k, *a = [int(x) for x in sys.stdin.read().split()]

    l = r = 0
    total = 0
    while True:
        if sum(a[l:r+1]) < k:
            if r == n-1:
                break
            else:
                r += 1
        else:
            total += n - r
            l += 1
    print(total)

if __name__ == "__main__":
    main()
