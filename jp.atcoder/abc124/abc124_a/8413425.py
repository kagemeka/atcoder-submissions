# 2019-11-13 01:34:25(JST)
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
    a, b = [int(x) for x in sys.stdin.readline().split()]
    if a == b:
        ans = a + b
    elif a > b:
        ans = a + (a - 1)
    elif b > a:
        ans = b + (b - 1)

    print(ans)



if __name__ == "__main__":
    main()
