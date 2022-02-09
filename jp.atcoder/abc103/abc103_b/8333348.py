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
# import functools
# import operator
## from external libraries
# import scipy.special   # if use comb function on AtCoder,
# import scipy.misc      # select scipy.misc.comb (old version)


def stringRotation(s):
    # |s| must be more than 1
    return s[-1] + s[:-1]


def main():
    s, t = sys.stdin.read().split()
    for _ in range(len(s)):
        if s == t:
            ans = 'Yes'
            break
        s = stringRotation(s)
    else:
        ans = 'No'

    print(ans)



if __name__ == "__main__":
    # execute only if run as a script
    main()
