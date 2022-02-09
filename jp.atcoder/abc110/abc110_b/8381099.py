# 2019-11-10 15:45:20(JST)
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
    n, m, X, Y = (int(i) for i in sys.stdin.readline().split())
    x = [int(x) for x in sys.stdin.readline().split()]
    y = [int(y) for y in sys.stdin.readline().split()]
    max_x = max(x + [X])
    min_y = min(y + [Y])
    if Y - X < 1 or min_y - max_x < 1:
        ans = 'War'
    else:
        ans = 'No War'

    print(ans)

if __name__ == "__main__":
    main()
