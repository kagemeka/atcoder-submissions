# 2019-11-15 14:37:47(JST)
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
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]
    at_beginning = sum(a)
    for i in range(n):
        if a[i] >= b[i]:
            a[i] -= b[i]
        else:
            a[i+1] = max(0, a[i+1] - (b[i] - a[i]))
            a[i] = 0

    at_ending = sum(a)

    ans = at_beginning - at_ending
    print(ans)


if __name__ == "__main__":
    main()
