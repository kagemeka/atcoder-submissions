# 2019-11-15 14:12:24(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, *a = [int(x) for x in sys.stdin.read().split()]
    a = [None] + a

    in_or_not = [0 for _ in range(n+1)]
    for i in range(n, 0, -1):
        count = sum(in_or_not[2*i:n+1:i])
        in_or_not[i] = a[i] ^ count % 2

    print(in_or_not.count(1))
    for i in range(1, n+1):
        if in_or_not[i] == 1:
            print(i, end=' ')


if __name__ == "__main__":
    main()
