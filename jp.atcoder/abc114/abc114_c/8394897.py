# 2019-11-11 16:07:35(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

shichigosan = '357'

def main():

    n = int(sys.stdin.readline().rstrip())

    count = 0
    for i in range(3, len(str(n)) + 1):
        sub_shichigosan = list(''.join(s) for s in itertools.product(shichigosan, repeat=i))
        for sub in sub_shichigosan:
            for d in shichigosan:
                if d in sub:
                    continue
                else:
                    break
            else:
                if 357 <= int(sub) <= n:
                    count += 1

    print(count)

if __name__ == "__main__":
    main()
