# 2019-11-15 14:12:24(JST)
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
    n, *a = [int(x) for x in sys.stdin.read().split()]
    b = a.copy()
    b.sort()
    largest = b[-1]
    second_largest = None
    if b[-2] == largest:
        pass
    else:
        second_largest = b[-2]

    if not second_largest:
        for i in range(n):
            print(largest)
    else:
        for i in range(n):
            if a[i] == largest:
                print(second_largest)
            else:
                print(largest)


if __name__ == "__main__":
    main()
