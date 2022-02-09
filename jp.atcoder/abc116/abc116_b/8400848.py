# 2019-11-12 01:01:32(JST)
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

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def main():
    s = int(sys.stdin.readline().rstrip())

    a = []
    n = s
    m = 1
    while True:
        a.append(n)
        n = f(n)
        m +=1
        if n in a:
            print(m)
            break


if __name__ == "__main__":
    main()
