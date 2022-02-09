# 2019-11-14 10:01:24(JST)
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

mod = 10 ** 9 + 7
def main():
    n, m, *broken_treads = [int(x) for x in sys.stdin.read().split()]
    safe = sorted((set(range(1, n+1)) - set(broken_treads)))

    case = []
    p_pre_pre = 0
    p_pre = 1 # 0th step
    count = 0
    continuous_broken_count = 0
    for i in range(1, n+1):
        if i in safe:
            continuous_broken_count = 0
            count += 1
            if count % 2 == 1:
                p_pre_pre = p_pre + p_pre_pre
            else:
                p_pre = p_pre_pre + p_pre
        elif count != 0:
            continuous_broken_count = 1
            if count % 2 == 1:
                case.append(p_pre_pre)
            else:
                case.append(p_pre)
            p_pre_pre = 1
            p_pre = 0
            count = 0
        else:
            continuous_broken_count += 1
            if continuous_broken_count == 2:
                print(0)
                sys.exit()
            p_pre_pre = 1
            p_pre = 0

    if count != 0:      # if n-th tread is not broken.
        if count % 2 == 1:
            case.append(p_pre_pre)
        else:
            case.append(p_pre)

    ans = 1
    for c in case:
        ans = (ans * c) % mod
    print(ans)


if __name__ == "__main__":
    main()
