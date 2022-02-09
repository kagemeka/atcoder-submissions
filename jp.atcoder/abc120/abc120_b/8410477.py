# 2019-11-12 21:58:02(JST)
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
    a, b, k = [int(x) for x in sys.stdin.readline().split()]
    n = 1
    count = 0
    while True:
        if a % n == 0 and b % n == 0:
            count += 1
            if count == k:
                print(n)
                sys.exit()
        n += 1


if __name__ == "__main__":
    main()
