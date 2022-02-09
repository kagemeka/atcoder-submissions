# 2019-11-12 15:53:47(JST)
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
    nm, *lines = sys.stdin.readlines()
    n, m = [int(x) for x in nm.split()]
    likes = [[int(x) for x in line.split()] for line in lines]
    menu = set(range(1, m+1))
    res = menu
    print(res)
    for i in range(n):
        res &= set(likes[i][1:])
        print(res)

    print(len(res))

if __name__ == "__main__":
    main()
