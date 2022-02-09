# 2019-11-19 19:43:48(JST)
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

table = set()
for i in range(1, 10):
    for j in range(i, 10):
        table.add(i * j)

def main():
    n = int(sys.stdin.readline().rstrip())

    print('Yes' if n in table else 'No')


if __name__ == "__main__":
    main()
