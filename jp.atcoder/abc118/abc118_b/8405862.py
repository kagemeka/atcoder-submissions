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
    nm, *likes = [line.rstrip() for line in sys.stdin.readlines()]
    n, m = [int(x) for x in nm.split()]
    menu = set(str(i) for i in range(1, m+1))
    res = menu
    for i in range(n):
        res &= set(likes[i][1:])

    print(len(res))

if __name__ == "__main__":
    main()
