# 2019-11-12 22:11:12(JST)
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
    H, W, h, w = [int(x) for x in sys.stdin.read().split()]

    ans = H * W - (h * W + (H - h) * w)
    print(ans)



if __name__ == "__main__":
    main()
