# 2019-11-11 16:07:35(JST)
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

like = 753
def main():
    S = sys.stdin.readline().rstrip()
    min_diff = 642
    for i in range(len(S)-2):
        x = int(S[i:i+3])
        diff = abs(753 - x)
        min_diff = min(min_diff, diff)
    print(min_diff)

if __name__ == "__main__":
    main()
