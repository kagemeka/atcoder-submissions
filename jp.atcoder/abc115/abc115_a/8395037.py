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
    d = int(sys.stdin.readline().rstrip())
    ans = 'Christmas'
    if d <= 24:
        ans += ' Eve'
    if d <= 23:
        ans += ' Eve'
    if d == 22:
        ans += ' Eve'
    print(ans)


if __name__ == "__main__":
    main()
