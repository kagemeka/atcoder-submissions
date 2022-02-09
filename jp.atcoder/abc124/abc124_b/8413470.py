# 2019-11-13 01:34:25(JST)
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
    n, *h = [int(x) for x in sys.stdin.read().split()]

    count = 0
    for i in range(n):
        if max(h[:i+1]) <= h[i]:
            count += 1

    print(count)



if __name__ == "__main__":
    main()
