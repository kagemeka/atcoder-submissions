# 2019-11-20 21:11:21(JST)
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
    s = sys.stdin.readline().rstrip()

    if len(s) == 1:
        print('YES')
        sys.exit()

    c = collections.Counter(s).values()
    if len(c) == 1:
        ans = 'NO'
    elif len(c) == 2:
        if len(s) == 2:
            ans = 'YES'
        else:
            ans = 'NO'
    else:
        if max(c) - min(c) >= 2:
            ans = 'NO'
        else:
            ans = 'YES'

    print(ans)
if __name__ == "__main__":
    main()
