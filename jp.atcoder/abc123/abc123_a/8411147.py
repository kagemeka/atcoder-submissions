# 2019-11-12 22:40:44(JST)
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
    *antennas, k = [int(x) for x in sys.stdin.read().split()]
    if antennas[-1] - antennas[0] > k:
            print(':(')
            sys.exit()
    print('Yay!')

if __name__ == "__main__":
    main()
