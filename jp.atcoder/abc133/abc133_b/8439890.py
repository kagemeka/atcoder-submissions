# 2019-11-15 13:51:51(JST)
import sys
# import collections
import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, d = [int(x) for x in sys.stdin.readline().split()]
    x = [tuple(int(x) for x in sys.stdin.readline().split()) for _ in range(n)]

    count = 0
    for i in range(n-1):
        for j in range(1, (n-1)-i+1):
            dist = sum([ (x[i+j][k] - x[i][k]) ** 2 for k in range(d)]) ** 0.5
            if dist == math.floor(dist):
                count += 1

    print(count)

if __name__ == "__main__":
    main()
