# 2019-11-15 13:51:51(JST)
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
    n, a, b = [int(x) for x in sys.stdin.readline().split()]
    if n * a >= b:
        ans = b
    else:
        ans = n * a

    print(ans)


if __name__ == "__main__":
    main()
