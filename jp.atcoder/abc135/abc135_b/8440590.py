# 2019-11-15 14:37:47(JST)
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
    n, *p = [int(x) for x in sys.stdin.read().split()]

    for i in range(n):
        if p[i] != i + 1:
            if p[p[i]-1] == i + 1:
                p[p[i]-1], p[i] = p[i], i+1
            break

    print('Yes' if p == list(range(1, n+1)) else 'No')


if __name__ == "__main__":
    main()
