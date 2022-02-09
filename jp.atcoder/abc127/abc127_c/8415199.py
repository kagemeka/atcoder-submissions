# 2019-11-13 08:30:54(JST)
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
    n, m = [int(x) for x in sys.stdin.readline().split()]

    l, r = [], []
    for _ in range(m):
        li, ri = [int(x) for x in sys.stdin.readline().split()]
        l.append(li)
        r.append(ri)

    print(min(r) - max(l) + 1 if min(r) >= max(l) else 0)



if __name__ == "__main__":
    main()
