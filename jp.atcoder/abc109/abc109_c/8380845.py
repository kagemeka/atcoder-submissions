#                         author:  kagemeka
#                         created: 2019-11-10 12:28:14(JST)
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
# import scipy.special
# import scipy.misc
# import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    n, *x = (int(i) for i in sys.stdin.read().split())

    res = functools.reduce(gcd, [abs(x[i+1] - x[i]) for i in range(n)])

    print(res)

if __name__ == "__main__":
    # execute only if run as a script
    main()
