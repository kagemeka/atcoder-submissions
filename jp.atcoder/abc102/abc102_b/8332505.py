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
# import statistics
# import functools
# import operator
## external modules
# import scipy.special   # if use comb function on AtCoder,
# import scipy.misc      # select scipy.misc.comb (old version)

def main():
    n, *a = (int(x) for x in sys.stdin.read().split())
    a.sort()
    print(a[-1] - a[0])


if __name__ == "__main__":
    # execute only if run as a script
    main()
