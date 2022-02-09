# 2019-11-16 10:55:08(JST)
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
    n, *h = [int(x) for x in sys.stdin.read().split()]


    ans = 'Yes'
    maximum = h[0]
    for i in range(1, n):
        if maximum - h[i] >= 2:
            ans = 'No'
            break
        maximum = max(maximum, h[i])

    print(ans)




if __name__ == "__main__":
    main()
