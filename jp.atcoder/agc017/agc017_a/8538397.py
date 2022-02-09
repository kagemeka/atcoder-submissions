# 2019-11-20 21:35:12(JST)
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
from scipy.misc import comb # (default: exact=False)
import numpy as np


def main():
    n, p = [int(x) for x in sys.stdin.readline().split()]
    a = np.array(sys.stdin.readline().split(), np.int64)
    a %= 2
    a.sort()
    count0 = np.searchsorted(a, 1)
    count1 = n - count0

    ans = 0
    if p == 1:
        for i in range(count0+1):
            for j in range(1, count1+1, 2):
                ans += comb(count0, i, exact=True) * comb(count1, j, exact=True)
    else:
        for i in range(count0+1):
            for j in range(0, count1+1, 2):
                ans += comb(count0, i, exact=True) * comb(count1, j, exact=True)

    print(ans)





if __name__ == "__main__":
    main()
