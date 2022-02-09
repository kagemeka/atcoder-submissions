# 2019-11-12 22:40:44(JST)
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
    dishes = [int(x) for x in sys.stdin.read().split()]
    min_first_digit = min(dishes[i] % 10 for i in range(5) if dishes[i] % 10 != 0) | 0

    total = 0
    for i in range(5):
        if dishes[i] % 10 != 0:
            total += (dishes[i] // 10 + 1) * 10
        else:
            total += dishes[i]

    ans = total - (10 - min_first_digit)
    print(ans)

if __name__ == "__main__":
    main()
