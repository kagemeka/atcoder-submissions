# 2019-11-12 22:11:12(JST)
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
    n, m, c = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]
    a = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]

    count = 0
    for i in range(n):
        s = c
        for j in range(m):
            s += b[j] * a[i][j]
        if s > 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
