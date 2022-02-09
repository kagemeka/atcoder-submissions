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

    pattern_for_each_section = []
    ans = 1
    p = [0, 1]
    continuous_broken_count = 0
    for i in range(1, n+1):
        if i in safe:
            continuous_broken_count = 0
            p.append(p[-1] + p[-2])
        else:
            continuous_broken_count += 1
            if continuous_broken_count == 1:
                pattern_for_each_section.append(p[-1])
                p = [1, 0]
            else:
                print(0)
                sys.exit()

    if continuous_broken_count == 0:
        pattern_for_each_section.append(p[-1])


    for c in pattern_for_each_section:
        ans = ans * c % mod
    print(ans)


if __name__ == "__main__":
    main()
