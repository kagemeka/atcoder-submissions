# 2019-11-17 10:52:21(JST)
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
    s, t = [s.rstrip() for s in sys.stdin.read().split()]

    if set(t) - set(s):
        print(-1)
        sys.exit()

    count = 0
    l = 0
    i = 0
    current = t[i]
    all_found = False
    while not all_found:
        j = s.find(current, l, len(s))
        if j == -1:
            count += len(s)
            l = 0
        else:
            if i == len(t) - 1:
                count += j + 1
                all_found = True
            else:
                if j == len(s) - 1:
                    count += len(s)
                    l = 0
                else:
                    l = j + 1
                i += 1
                current = t[i]
    print(count)



if __name__ == "__main__":
    main()
