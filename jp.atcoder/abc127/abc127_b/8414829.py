# 2019-11-13 08:30:54(JST)
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
    r, d, x0 = [int(x) for x in sys.stdin.readline().split()]
    x = x0
    for _ in range(10):
        x = r * x - d
        print(x)

if __name__ == "__main__":
    main()
