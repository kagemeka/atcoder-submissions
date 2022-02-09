# 2019-11-14 20:54:46(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, l = [int(x) for x in sys.stdin.readline().split()]
    flavors = []
    for i in range(1, n+1):
        flavors.append(l + i - 1)
    # key=function  要素にfunctionを適用した戻り値でsortする
    flavors.sort(key=abs)
    print(sum(flavors[1:]))

if __name__ == "__main__":
    main()
