# 2019-11-13 21:06:16(JST)
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
    n = int(sys.stdin.readline().rstrip())

    order = []
    cities = []
    for i in range(1, n+1):
        city, score = sys.stdin.readline().split()
        order.append([city, int(score), i])
        cities.append(city)

    res = dict((c, list()) for c in set(cities))
    for i in range(n):
        res[order[i][0]].append(order[i][1:])

    for city, score in sorted(res.items()):
        for s in sorted(score, reverse=True):
            print(s[1])

if __name__ == "__main__":
    main()
