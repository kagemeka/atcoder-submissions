# 2019-11-10 17:11:42(JST)
import sys
import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
import operator as op
# from scipy.misc import comb # float
# import numpy as np
# import statistics

def main():

    n, *v = (int(x) for x in sys.stdin.read().split())

    odds, evens = [], []
    for i in range(n):
        if i % 2 == 0:
            odds.append(v[i])
        else:
            evens.append(v[i])


    o_c = collections.Counter(odds)
    e_c = collections.Counter(evens)

    o_c = sorted(list((k, v) for k, v in o_c.items()), key=op.itemgetter(1), reverse=True)
    e_c = sorted(list((k, v) for k, v in e_c.items()), key=op.itemgetter(1), reverse=True)

    ans = n
    if o_c[0][0] != e_c[0][0]:
        ans = n - o_c[0][1] - e_c[0][1]
    else:
        if len(o_c) == 1 and len(e_c) == 1:
            ans = n - n // 2
        elif len(o_c) == 1 and len(e_c) >= 2:
            ans = n - e_c[1][1]
        elif len(o_c) >= 2 and len(e_c) == 1:
            ans = n - o_c[1][1]
        else:
            ans = n - max(o_c[0][1] + e_c[1][1], o_c[1][1] + e_c[0][1])

    print(ans)

if __name__ == "__main__":
    main()
