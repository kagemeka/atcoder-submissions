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

        left = x[i]
        right = x[i + k - 1]
        mi = min(abs(left) + abs(right - left), abs(right) + abs(left - right))
        minimums.append(mi)

    ans = min(minimums)
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
