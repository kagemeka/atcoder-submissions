# 2019-11-20 14:30:57(JST)
import sys
import collections
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
    score = [int(x) for x in sys.stdin.read().split()]
    rank = sorted(score, reverse=True)
    c = collections.defaultdict(int)
    for i in range(len(score)):
        c[rank[i]] += i + 1

    for s in score:
        print(c[s])


if __name__ == "__main__":
    main()
