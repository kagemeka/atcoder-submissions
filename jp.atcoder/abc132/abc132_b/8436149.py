# 2019-11-15 00:35:39(JST)
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
    n, *p = [int(x) for x in sys.stdin.read().split()]

    compare = []
    for i in range(n-1):
        if p[i] < p[i+1]:
            compare.append('<')
        else:
            compare.append('>')

    count = 0
    for i in range(1, n-1):
        if compare[i-1] == compare[i] == '<' or compare[i-1] == compare[i] == '>':
            count += 1

    print(count)

if __name__ == "__main__":
    main()
