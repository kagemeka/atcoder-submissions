# 2019-11-20 22:09:02(JST)
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
    n, W, *VW = [int(x) for x in sys.stdin.read().split()]
    v, w = VW[0:n * 2:2], VW[1:n * 2:2]

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(W+1):
            if w[i] > j:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])
    print(dp[n][W])


if __name__ == "__main__":
    main()
