# 2019-11-17 10:52:21(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np


def main():
    n, *v = [int(x) for x in sys.stdin.read().split()]
    v.sort()

    ans = (1/2)**(n-1) * (v[0] + sum(v[i] * 2**(i-1) for i in range(1, n)))
    print(ans)


if __name__ == "__main__":
    main()
