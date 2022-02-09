# 2019-11-13 01:53:22(JST)
import sys
# import collections
import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]


    probability = 0
    for i in range(1, n + 1):
        if i < k:
            probability += (1 / n) * (1 / 2) ** math.ceil(math.log2(k / i))
        else:
            probability += 1 / n

    print(probability)

if __name__ == "__main__":
    main()
