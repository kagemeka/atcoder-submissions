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
    n, k, *A = [int(x) for x in sys.stdin.read().split()]

    total = 0
    for i in range(n):
        total += n - i - bi_l(list(itertools.accumulate(A[i:])), k)

    print(total)

if __name__ == "__main__":
    main()
