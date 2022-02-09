# 2019-11-11 14:35:02(JST)
import sys
# import collections
import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np
from copy import deepcopy

def main():
    n, m = (int(x) for x in sys.stdin.readline().split())
    PY = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
    py = sorted(deepcopy(PY))

    ids = dict()
    for i in range(m):
        p, y = py[i][0], py[i][1]
        if not p in ids:
            ids[p] = dict()
            x = 0
        x += 1
        id_i = '0' * (6 - (math.floor(math.log10(p)) + 1)) + str(p) + '0' * (6 - (math.floor(math.log10(x)) + 1)) + str(x)
        ids[p][y] = id_i

    for i in range(m):
        p, y = PY[i][0], PY[i][1]
        print(ids[p][y])


if __name__ == "__main__":
    main()
