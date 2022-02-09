# 2019-11-13 08:30:54(JST)
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
    n, m = [int(x) for x in sys.stdin.readline().split()]

    l, r = [], []
    for i in range(m):
        li, ri = [int(x) for x in sys.stdin.readline().split()]
        l.append(li)
        r.append(ri)

    # all_mighty_cards = set(range(1,n+1))
    # for i in range(m):
    #     all_mighty_cards &= set(l[i:] + r[:i+1])



    # print(len(all_mighty_cards) if all_mighty_cards else 0)

    print(r[0] - l[-1] + 1)



if __name__ == "__main__":
    main()
