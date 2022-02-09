# 2019-11-15 00:35:39(JST)
import sys
import collections
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
    for v in collections.Counter(s).values():
        if v == 2:
            continue
        else:
            ans = 'No'
            break
    else:
        ans = 'Yes'

    print(ans)

if __name__ == "__main__":
    main()
