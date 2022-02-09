# 2019-11-15 00:35:39(JST)
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
    n, *difficulties = [int(x) for x in sys.stdin.read().split()]
    difficulties.sort()

    ans = difficulties[n // 2] - difficulties[n // 2 - 1]
    print(ans)

if __name__ == "__main__":
    main()
