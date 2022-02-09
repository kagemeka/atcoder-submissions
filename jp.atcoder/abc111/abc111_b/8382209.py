# 2019-11-10 17:11:42(JST)
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
    for i in range(1, 10):
        nex = int(str(i) * 3)
        if nex >= n:
            ans = nex
            break

    print(ans)

if __name__ == "__main__":
    main()
