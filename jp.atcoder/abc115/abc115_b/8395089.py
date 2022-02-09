# 2019-11-11 18:30:26(JST)
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
    n, *p = (int(x) for x in sys.stdin.read().split())
    total_cost = sum(p) - max(p) // 2
    print(total_cost)


if __name__ == "__main__":
    main()
