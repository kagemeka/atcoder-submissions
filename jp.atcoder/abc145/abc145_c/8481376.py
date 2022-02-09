# 2019-11-16 21:01:15(JST)
import sys
# import collections
import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def dist(x1,y1,x2,y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def main():
    n = int(sys.stdin.readline().rstrip())
    x, y = [], []
    for _ in range(n):
        xi, yi = [int(x) for x in sys.stdin.readline().split()]
        x.append(xi)
        y.append(yi)

    ans = 0
    for p in itertools.permutations(range(n), n):
        d = 0
        for i in range(n-1):
            d += dist(x[p[i]], y[p[i]], x[p[i+1]], y[p[i+1]])
        ans += d

    ans /= math.factorial(n)
    print(ans)


if __name__ == "__main__":
    main()
