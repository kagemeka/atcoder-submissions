# 2019-11-14 20:54:46(JST)
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
    s = sys.stdin.readline().rstrip()
    for i in range(3):
        if s[i] == s[i+1]:
            ans = 'Bad'
            break
    else:
        ans = 'Good'

    print(ans)


if __name__ == "__main__":
    main()
