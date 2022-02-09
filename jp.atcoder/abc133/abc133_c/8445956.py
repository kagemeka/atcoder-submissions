# 2019-11-15 13:51:51(JST)
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

mod = 2019

def main():
    l, r = [int(x) for x in sys.stdin.readline().split()]

    if l + 2019 <= r:
        m = l + 2018
    else:
        m = r

    remainders = []
    for i in range(l, m):
        for j in range(i+1, m+1):
            remainders.append(i * j % mod)

    print(min(remainders))

if __name__ == "__main__":
    main()
