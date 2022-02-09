# 2019-11-13 21:06:16(JST)
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
    a, p = [int(x) for x in sys.stdin.readline().split()]
    pieces = a * 3 + p
    pies = pieces // 2
    print(pies)

if __name__ == "__main__":
    main()
