#                         author:  kagemeka
#                         created: 2019-11-09 11:51:37(JST)
### modules
## from standard library
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator
## from external libraries
# import scipy.special
# import scipy.misc
# import numpy as np


def baseConvert(n, base):
    if n == 0:
        return ''
    else:
        for i in range(abs(base)):
            if n % abs(base) == i:
                return baseConvert((n - i) // base, base) + str(i)

def main():
    n = int(sys.stdin.readline().rstrip())
    base = -2

    if n == 0:
        ans = '0'
    else:
        ans = baseConvert(n, base)
    print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
