# 2019-11-13 01:53:22(JST)
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
    first, second = int(s[:2]), int(s[2:])
    if 1 <= first <= 12:
        if 1 <= second <= 12:
            ans = 'AMBIGUOUS'
        else:
            ans = 'MMYY'
    else:
        if 1 <= second <= 12:
            ans = 'YYMM'
        else:
            ans = 'NA'
    print(ans)



if __name__ == "__main__":
    main()
