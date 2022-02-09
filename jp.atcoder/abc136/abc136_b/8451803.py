# 2019-11-16 10:55:08(JST)
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
    n = int(sys.stdin.readline().rstrip())

    if  math.floor(math.log10(n)) % 2 == 0:
        ans = n
    else:
        ans = 10 ** (math.floor(math.log10(n))+1) - 1
    for i in range(1, math.floor(math.log10(n)+1), 2):
        ans -= 10 ** (i+1) - 1 - 10 ** i + 1

    print(ans)

if __name__ == "__main__":
    main()
