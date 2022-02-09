# 2019-11-13 08:30:54(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    a.sort()

    replace = []
    for _ in range(m):
        bi, ci = [int(x) for x in sys.stdin.readline().split()]
        replace += [ci] * bi

    replace.sort(reverse=True)

    for i in range(n):
        if i < len(replace):
            if a[i]< replace[i]:
                a[i] = replace[i]
                continue
            else:
                break
        else:
            break

    print(sum(a))



if __name__ == "__main__":
    main()
