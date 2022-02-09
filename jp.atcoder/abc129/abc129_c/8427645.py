# 2019-11-14 10:01:24(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

mod = 10 ** 9 + 7
def main():
    n, m, *broken_treads = [int(x) for x in sys.stdin.read().split()]
    safe = sorted((set(range(1, n+1)) - set(broken_treads)))

    p = [0] * (n + 1) # p[i] は連続するi段の、1~i段目までの登り方の総パターン
    p[1] = 1
    for i in range(2, n+1):
        p[i] = p[i-1] + p[i-2]

    count = 1 # 最初に0th stepを踏んでいるので1
    sections = []
    for i in range(1, n+1):
        if i in safe:
            count += 1
        else:
            if count >= 1:
                sections.append(p[count])
                count = 0
            else: # countが0だったら一つ前も壊れている
                print(0)
                sys.exit()

    if count >= 1:    # if the last is not broken.
        sections.append(p[count])

    ans = reduce(lambda x, y: x * y % mod, sections)
    print(ans)

if __name__ == "__main__":
    main()
