#                         author:  kagemeka
#                         created: 2019-11-09 21:20:16(JST)
### modules
## from standard library
import sys
# import collections
# import math
# import string
import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator
## from external libraries
# import scipy.special
# import scipy.misc
# import numpy as np

mod = 998244353

def main():
    n, *d = (int(x) for x in sys.stdin.read().split())

    if d[0] != 0:
        print(0)
        exit()

    del d[0]

    if 0 in d:
        print(0)
        exit()

    d.sort()

    maximum = d[-1]
    for i in range(1, maximum + 1):
        if not i in d:
            print(0)
            exit()

    total = 1
    for i in range(1, maximum):
        base = bisect.bisect_right(d, i) - bisect.bisect_left(d, i)
        exp = bisect.bisect_right(d, i+1) - bisect.bisect_left(d, i+1)
        total *= (base ** exp)
    print(total % mod)



if __name__ == "__main__":
    # execute only if run as a script
    main()
