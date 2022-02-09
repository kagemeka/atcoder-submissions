# 2019-11-12 01:01:32(JST)
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
    n, *h = (int(x) for x in sys.stdin.read().split())

    mountain = []
    valley = []
    flat = 0
    i = 0
    while True:
        if h[i] == h[i+1]:
            i += 1
            continue
        elif h[i] < h[i+1]:
            break
        else:
            mountain.append(h[i])
            break
    i = -1
    while True:
        if h[i-1] == h[i]:
            i -= 1
            continue
        elif h[i-1] > h[i]:
            break
        else:
            mountain.append(h[i])
            break
    for i in range(1, n-1):
        if flat == 0:
            if h[i-1] < h[i] > h[i+1]:
                mountain.append(h[i])
            elif h[i-1] > h[i] < h[i+1]:
                valley.append(h[i])
            elif h[i-1] < h[i] == h[i+1]:
                flat = 1
            elif h[i-1] > h[i] == h[i+1]:
                flat = -1
        else:
            if flat == 1:
                if h[i] > h[i+1]:
                    mountain.append(h[i])
                    flat = 0
                elif h[i] < h[i+1]:
                    flat = 0
            elif flat == -1:
                if h[i] < h[i+1]:
                    valley.append(h[i])
                    flat = 0
                elif h[i] > h[h+1]:
                    flat = 0


    ans = sum(mountain) - sum(valley)
    print(ans)


if __name__ == "__main__":
    main()
