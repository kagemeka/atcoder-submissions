# 2019-11-10 17:11:42(JST)
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
    n = list(sys.stdin.readline().rstrip())
    for i in range(len(n)):
        if n[i] == '9':
            n[i] = '1'
        else:
            n[i] ='9'


    print(''.join(n))

if __name__ == "__main__":
    main()
