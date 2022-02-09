# 2019-11-13 08:30:54(JST)
import sys
import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]

    a = list(collections.Counter(a).items())

    for _ in range(m):
        b, c = [int(x) for x in sys.stdin.readline().split()]
        a.append((c,b))

    a.sort(reverse=True)

    total = 0
    count = 0
    for i in range(n+m): # max
        select = a[i]
        for j in range(select[1], 0, -1):
            if count + j > n:
                continue
            else:
                count += j
                total += select[0] * j
                break
        if count == n:
            break

    print(total)

if __name__ == "__main__":
    main()
