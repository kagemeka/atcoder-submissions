# 2019-11-13 01:53:22(JST)
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
    n, k = [int(x) for x in sys.stdin.readline().split()]
    s = list(sys.stdin.readline().rstrip())
    s[k-1] = s[k-1].lower()
    print(''.join(s))



if __name__ == "__main__":
    main()
