# 2019-11-16 14:51:41(JST)
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
    ans = max(a+b, a-b, a*b)
    print(ans)


if __name__ == "__main__":
    main()
