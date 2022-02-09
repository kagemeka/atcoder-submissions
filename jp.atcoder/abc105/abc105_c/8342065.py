-9
#                         author:  kagemeka
#                         created: 2019-11-09 11:51:37(JST)
### modules
## from standard library
import sys
# import collections
import math
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


def f(n):
    if n == 0:
        return ''
    else:
        if n % 2 == 0:
            return f(n // (-2)) + '0'
        else:
            return f((n - 1) // (-2)) + '1'


def main():
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        ans = '0'
    else:
        ans = f(n)
    print(ans)






if __name__ == "__main__":
    # execute only if run as a script
    main()
