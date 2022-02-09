# 2019-11-16 21:01:15(JST)
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
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    if n % 2 == 1:
        ans = 'No'
    else:
        if s[:n//2] * 2 == s:
            ans = 'Yes'
        else:
            ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
