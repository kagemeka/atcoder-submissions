# 2019-11-12 22:21:08(JST)
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
    s = sys.stdin.readline().rstrip()

    permitted = 'ACGT'
    continuous_count = []
    count = 0

    for i in range(len(s)):
        char = s[i]
        if char in permitted:
            count += 1
        else:
            continuous_count.append(count)
            count = 0
        if i == len(s) - 1:
            continuous_count.append(count)

    if not continuous_count:
        print(len(s))
    else:
        print(max(continuous_count))



if __name__ == "__main__":
    main()
