# 2019-11-19 10:28:31(JST)
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
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np


def main():
    n, m, l = map(int, sys.stdin.readline().split())
    ABCQST = np.array(sys.stdin.read().split(), np.int64)
    ABC = ABCQST[:m * 3]
    A, B, C = ABC[::3], ABC[1::3], ABC[2::3]
    ST = ABCQST[m * 3 + 1:]
    S, T = ST[::2], ST[1::2]

    dist = csr_matrix((C, (A, B)), (n+1, n+1))
    min_dist = floyd_warshall(dist, directed=False)

    filling_times = np.full((n+1, n+1), np.inf)
    np.diagonal(filling_times, 0)
    filling_times[min_dist <= l] = 1

    min_filling_times = floyd_warshall(filling_times, directed=False)

    min_filling_times[min_filling_times == np.inf] = 0
    # 最後に-1する
    min_filling_times = min_filling_times.astype(int)

    res = min_filling_times[S, T] - 1
    print('\n'.join(res.astype(str)))


if __name__ == "__main__":
    main()
