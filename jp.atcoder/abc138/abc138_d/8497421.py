# 2019-11-17 10:52:21(JST)
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
    n, q = [int(x) for x in sys.stdin.readline().split()]
    AB = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        AB[a].append(b)

    ans = [0 for _ in range(n+1)]
    for _ in range(q):
        p, x = [int(x) for x in sys.stdin.readline().split()]
        ans[p] += x

    for a in range(1, n):
        for b in AB[a]:
            ans[b] += ans[a]

    print(' '.join(map(str, ans[1:])))

if __name__ == "__main__":
    main()
