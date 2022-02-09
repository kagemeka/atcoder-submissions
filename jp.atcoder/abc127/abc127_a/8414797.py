# 2019-11-13 08:30:54(JST)
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
    a, b = [int(x) for x in sys.stdin.readline().split()]
    if a >= 13:
        ans = b
    elif a >= 6:
        ans = b // 2
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
