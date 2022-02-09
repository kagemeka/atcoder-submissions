# 2019-11-13 08:30:54(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    a.sort()

    bc = []
    for _ in range(m):
        bi, ci = [int(x) for x in sys.stdin.readline().split()]
        bc.append([bi, ci])

    bc.sort(reverse=True, key=lambda x: x[1])

    res = []
    for i in range(m):
        if a:
            index = bi_l(a, bc[i][1])
            if index == 0:
                res += a
                break
            else:
                if index > bc[i][0]:
                    a = a[bc[i][0]:]
                    res += [bc[i][1]] * bc[i][0]
                else:
                    a = a[index:]
                    res += [bc[i][1]] * index
        else:
            break
    else:
        res += a
    print(sum(res))


if __name__ == "__main__":
    main()
