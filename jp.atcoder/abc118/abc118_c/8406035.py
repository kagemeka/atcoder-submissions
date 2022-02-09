# 2019-11-12 15:53:47(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    n, *a = (int(x) for x in sys.stdin.read().split())

    ans = reduce(gcd, a)
    print(ans)



if __name__ == "__main__":
    main()
