# 2019-11-12 16:33:33(JST)
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
    mm = int(s[5:7])
    dd = int(s[8:10])
    if mm <= 4 and dd <= 30:
        print('Heisei')
    else:
        print('TBD')


if __name__ == "__main__":
    main()
