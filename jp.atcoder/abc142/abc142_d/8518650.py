# 2019-11-18 23:58:23(JST)
import sys
# import collections
import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np


def primeFactorize(n):
    from math import floor, sqrt
    res = set()
    before = n
    while n % 2 == 0:
        n //= 2
    if n < before:
        res.add(2)
    if n == 1:
        return res
    for i in range(3, floor(sqrt(n))+1, 2):
        before = n
        while n % i == 0:
            n //= i
        if n < before:
            res.add(i)
        if n == 1:
            return res
    res.add(n)
    return res

def main():
    a, b = [int(x) for x in sys.stdin.readline().split()]
    ans = len(primeFactorize(a) & primeFactorize(b)) + 1
    print(ans)

if __name__ == "__main__":
    main()
