#                         author:  kagemeka
#                         created: 2019-11-09 16:39:51(JST)
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

def main():
    n, k, *x = (int(i) for i in sys.stdin.read().split())

    minimums = []
    for i in range(n - k + 1):
        cur_range = x[i: i+k]
        if cur_range[-1] <= 0:
            mi = abs(cur_range[0])
        elif cur_range[0] >= 0:
            mi = abs(cur_range[-1])
        else:
            mi = min(abs(cur_range[0]) * 2 + cur_range[-1], abs(cur_range[0]) + cur_range[-1] * 2)
        minimums.append(mi)

    ans = min(minimums)
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
