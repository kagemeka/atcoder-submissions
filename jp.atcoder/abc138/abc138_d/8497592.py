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
        AB[b].append(a)
    # 無向グラフとして考える

    ans = [0 for _ in range(n+1)]
    for _ in range(q):
        p, x = [int(x) for x in sys.stdin.readline().split()]
        ans[p] += x

    stack = [1]
    parent = [0 for _ in range(n+1)]
    while stack:
        x = stack.pop()
        for y in AB[x]:
            if y != parent[x]: # yがxの親でなければ
                parent[y] = x # xがyの親
                stack.append(y)
                ans[y] += ans[x]


    print(' '.join(map(str, ans[1:])))

if __name__ == "__main__":
    main()
