# 2019-11-18 00:38:19(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np


def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    s = sys.stdin.readline().rstrip()

    # R を反転させる
    unhappy_count = 0
    if s[0] == 'L':
        unhappy_count += 1
    if s[-1] == 'R':
        unhappy_count += 1

    two_unhappy = [c.start() for c in re.finditer('RL', s)]

    unhappy_count += 2 * len(two_unhappy)
    if k >= len(two_unhappy):
        if 0 in two_unhappy:
            unhappy_count -= 1 + 2 * (len(two_unhappy) - 1)
        else:
            unhappy_count -= 2 * len(two_unhappy)
        unhappy_count = max(0, unhappy_count - (k - len(two_unhappy)))
    else:
        unhappy_count -= 2 * k

    happy_count = n - unhappy_count
    print(happy_count)

if __name__ == "__main__":
    main()
