# 2019-11-11 14:35:02(JST)
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
    n, T, A, *h = (int(x) for x in sys.stdin.read().split())

    min_diff, ans = abs(A - (T - h[0] * 0.006)), 1 # default
    for i in range(1, n):
        t = T - h[i] * 0.006
        diff = abs(A - t)
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)




if __name__ == "__main__":
    main()
