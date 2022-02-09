#                         author:  kagemeka
#                         created: 2019-11-08 14:51:29(JST)
## internal modules
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
import statistics
# import functools
# import operator
## external modules
# import scipy.special   # if use comb function on AtCoder,
# import scipy.misc      # select scipy.misc.comb (old version)

def main():
    n, *a = (int(x) for x in sys.stdin.read().split())

    for i in range(n):
        a[i] -= (i + 1)

    if n % 2 != 0:
        b = statistics.median(a)
    else:
        if a.count(statistics.median_high(a)) >= a.count(statistics.median_low(a)):
            b = statistics.median_high(a)
        else:
            b = statistics.median_low(a)

    ans = sum([abs(a[i] - b) for i in range(n)])
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
