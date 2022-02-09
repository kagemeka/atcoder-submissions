# 2019-11-18 00:38:19(JST)
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

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    s = sys.stdin.readline().rstrip()

    happy_count = sum([0] + [1 for i in range(n-1) if s[i] == s[i+1]])

    happy_count += 2 * k
    ans = min(happy_count, n - 1)
    print(ans)

if __name__ == "__main__":
    main()
