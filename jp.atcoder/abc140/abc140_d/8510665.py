# 2019-11-18 00:38:19(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
import numpy as np

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]

    s = np.array(list(sys.stdin.readline().rstrip()), dtype='U1')
    # dtype=U1 : Unicode, 1-char string.

    happy_count = np.count_nonzero(s[:-1] == s[1:])
    # s[:-1] と s[1:] の各要素を比較してTrue/False のndarray(n-dimensional array を返す)
    # np.count_nonzeroでcount(bool(elem) != False)を返す

    happy_count += 2 * k
    # every rotation make more two or one person happy.(editorial)

    happy_count = min(happy_count, n - 1)
    # finaly, at least one person is unhappy

    print(happy_count)

if __name__ == "__main__":
    main()
