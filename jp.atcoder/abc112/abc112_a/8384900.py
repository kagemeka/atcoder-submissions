# 2019-11-10 20:23:41(JST)
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
    if n == 1:
        print(1)
        sys.exit()
    else:
        a, b = (int(x) for x in sys.stdin.read().split())
        print(a + b)


if __name__ == "__main__":
    main()
