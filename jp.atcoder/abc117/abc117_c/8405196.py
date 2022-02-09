# 2019-11-12 13:20:54(JST)
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
    n, m, *x = (int(i) for i in sys.stdin.read().split())
    x.sort()
    if n >= m:
        print(0)
        sys.exit()

    ran = x[-1] - x[0] + 1
    quotient, remainder = ran // n, ran % n
    total_count = 0
    for i in range(x[0], x[-1-remainder], quotient):
        print(i)
        current = [j for j in x if i <= j < i + quotient]
        if not current:
            total_count -= 1
            continue
        count = max(current) - min(current)
        total_count += count

    total_count += remainder
    print(total_count)



if __name__ == "__main__":
    main()
