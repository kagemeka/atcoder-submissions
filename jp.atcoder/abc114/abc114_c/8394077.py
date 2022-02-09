# 2019-11-11 16:07:35(JST)
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

digits = ['3', '5', '7']

def main():
    # 357 以上
    # 3, 5, 7 のいずれかを使わない数字の個数をnから引けばいい
    n = int(sys.stdin.readline().rstrip())

    if n < 357:
        print(0)
        sys.exit()

    count = 0
    for m in range(357, n+1):
        m = str(m)
        c3, c5, c7 = 0, 0, 0
        for d in m:
            if d == '3':
                c3 += 1
            elif d == '5':
                c5 += 1
            elif d == '7':
                c7 += 1
            else:
                break
        else:
            if c3 >= 1 and c5 >= 1 and c7 >= 1:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
