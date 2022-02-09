# 2019-11-12 22:21:08(JST)
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
    b = sys.stdin.readline().rstrip()
    if b == 'A':
        ans = 'T'
    elif b == 'T':
        ans = 'A'
    elif b == 'G':
        ans = 'C'
    else:
        ans = 'G'

    print(ans)


if __name__ == "__main__":
    main()
