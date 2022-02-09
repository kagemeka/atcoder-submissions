# 2019-11-18 17:34:23(JST)
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
    n, s = sys.stdin.read().split()
    n = int(n)

    # a = [0 for _ in range(n)]
    # i = j = 0
    # while i < n:
    #     while i+j < n and s[j] == s[i+j]:
    #         j += 1
    #     a[i] = j
    #     if j == 0:
    #         i += 1
    #         continue
    #     k = 1
    #     while i+k < n and k+a[k] < j:
    #         a[i+k] = a[k]
    #         k += 1
    #     i += k
    #     j -= k

    # print(max(l for l in a if l <= n // 2))
    # print(a)

    ma = 0
    for k in range(n):
        sub = s[k:]
        a = [0 for _ in range(len(sub))]
        i, j = 1, 0
        while i < len(sub):
            while i+j < len(sub) and sub[j] == sub[i+j]:
                j += 1
                if j == len(sub) // 2:
                    break
            a[i] = j
            if j == 0:
                i += 1
                continue
            k = 1
            while i+k < len(sub) and k+a[k] < j:
                a[i+k] = a[k]
                k += 1
            i += k
            j -= k
        ma = max(ma, max(a))
    print(ma)

    # a = [0 for _ in range(n)]
    # a[0] = n
    # c = 0
    # for i in range(1, n):
    #     if i+a[i-c] < c+a[c]:
    #         a[i] = a[i-c]
    #     else:
    #         j = max(0, c+a[c]-i)
    #         while i+j < n and s[s] == s[i+j]:
    #             j += 1
    #         a[i] = j

    # print(a)

    # zz = [[0 for _ in range(n)] for _ in range(n)]

    # ans = [0 for _ in range(n)]
    # for k in range(n):
    #     # z = zz[k]
    #     z = [0 for _ in range(n)]
    #     sub = s[k:]
    #     for i in range(1, len(sub)):
    #         count = 0
    #         for j in range(len(sub)-i):
    #             if sub[j] == sub[i+j]:
    #                 count += 1
    #                 if count == n // 2:
    #                     break
    #             else:
    #                 break
    #         z[i] = count
    #     ans[k] = max(z)
    #     # zz[k] = z
    # print(max(ans))






if __name__ == "__main__":
    main()
