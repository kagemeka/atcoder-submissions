# 2019-11-20 23:47:42(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np


def main():
    H, W, n, *a = [int(x) for x in sys.stdin.read().split()]
    color_count = [None] + a

    canvas = [[None for _ in range(W)] for _ in range(H)]

    h, w = 0, 0
    for i in range(1, n+1):
        while color_count[i] > 0:
            canvas[h][w] = i
            color_count[i] -= 1

            if h % 2 == 0:
                w += 1
                if w == W:
                    h += 1
                    w = W - 1
            else:
                w -= 1
                if w == -1:
                    h += 1
                    w = 0

    for h in range(H):
        print(' '.join(map(str, canvas[h])))

if __name__ == "__main__":
    main()
