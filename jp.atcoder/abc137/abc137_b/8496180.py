# 2019-11-16 14:51:41(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    k, x = [int(x) for x in sys.stdin.readline().split()]
    stones = range(-10**6, 10**6+1)
    x_place = bi_l(stones, x)
    ans = stones[x_place-(k-1):x_place+(k-1)+1]
    for c in ans:
        print(c, end=' ')
    # k, x の制約から端を気にする必要はない
if __name__ == "__main__":
    main()
