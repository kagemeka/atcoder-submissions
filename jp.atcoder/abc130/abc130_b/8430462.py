# 2019-11-14 17:27:23(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, x, *l = [int(i) for i in sys.stdin.read().split()]

    culmative_sum = list(itertools.accumulate(l))
    ans = 1 + bi_r(culmative_sum, x)
    print(ans)

if __name__ == "__main__":
    main()
