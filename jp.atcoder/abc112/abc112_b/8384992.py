# 2019-11-10 20:23:41(JST)
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
    N, T = (int(x) for x in sys.stdin.readline().split())

    ct = []
    for i in range(N):
        c, t = (int(x) for x in sys.stdin.readline().split())
        if t <= T:
            ct.append((c, t))

    ct.sort()
    print(ct[0][0] if ct else 'TLE')


if __name__ == "__main__":
    main()
