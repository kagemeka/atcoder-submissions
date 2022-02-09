#                         author:  kagemeka
#                         created: 2019-11-08 15:54:47(JST)
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
import functools
# import operator
## from external libraries
# import scipy.special   # if use comb function on AtCoder,
# import scipy.misc      # select scipy.misc.comb (old version)
# import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    n, *a = (int(x) for x in sys.stdin.read().split())

    m = functools.reduce(lcm, a)
    f = sum([(m - 1) % a[i] for i in range(n)])
    print(f)

if __name__ == "__main__":
    # execute only if run as a script
    main()
