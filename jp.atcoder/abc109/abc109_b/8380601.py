#                         author:  kagemeka
#                         created: 2019-11-10 12:28:14(JST)
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
    n, *w = sys.stdin.read().split()
    n = int(n)
    for i in range(1, n):
        if w[i][0] == w[i-1][-1] and not w[i] in w[:i]:
            continue
        else:
            print('No')
            exit()

    print('Yes')


if __name__ == "__main__":
    # execute only if run as a script
    main()
