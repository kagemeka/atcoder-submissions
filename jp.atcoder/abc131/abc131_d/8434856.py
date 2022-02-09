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
    n = int(sys.stdin.readline().rstrip())
    ab = [tuple(int(x) for x in sys.stdin.readline().split()) for _ in range(n)]
    ab.sort(key=lambda x: x[1])

    s = 0
    for i in range(n):
        s += ab[i][0]
        if s <= ab[i][1]:
            continue
        else:
            ans = 'No'
            break
    else:
        ans = 'Yes'

    print(ans)

if __name__ == "__main__":
    main()
