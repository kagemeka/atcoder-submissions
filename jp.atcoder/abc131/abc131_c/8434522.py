# 2019-11-14 20:54:46(JST)
import sys
# import collections
import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    res1 = b - (b // c + b // d - b // lcm(c, d))
    res2 = (a - 1) - ((a - 1) // c + (a - 1) // d - (a - 1) // lcm(c, d))
    ans = res1 - res2
    print(ans)

if __name__ == "__main__":
    main()
