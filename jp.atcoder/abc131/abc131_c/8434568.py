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
    divisors = 0
    divisors += b // c - (a - 1) // c
    divisors += b // d - (a - 1) // d
    l = lcm(c, d)
    divisors -= b // l - (a - 1) // l
    ans = b - (a - 1) - divisors
    print(ans)



if __name__ == "__main__":
    main()
