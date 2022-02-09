# 2019-11-17 20:44:23(JST)
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
    n = int(sys.stdin.readline().rstrip())
    ans = (1 + (n - 1)) * (n - 1) // 2
    print(ans)
if __name__ == "__main__":
    main()
