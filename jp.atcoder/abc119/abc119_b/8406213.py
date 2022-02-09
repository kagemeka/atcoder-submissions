# 2019-11-12 16:33:33(JST)
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
    n = int(sys.stdin.readline().rstrip())

    otoshidamas = []
    for _ in range(n):
        x, u = sys.stdin.readline().split()
        x = float(x)
        otoshidamas.append([x, u])

    total = 0
    for i in range(n):
        if otoshidamas[i][1] == 'JPY':
            total += otoshidamas[i][0]
        else:
            total += otoshidamas[i][0] * 38e4

    print(total)


if __name__ == "__main__":
    main()
