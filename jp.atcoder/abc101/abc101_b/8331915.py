#                         author:  kagemeka
#                         created: 2019-11-08 13:38:56(JST)
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
    n = sys.stdin.readline().rstrip()
    s = sum([int(d) for d in n])
    print('Yes' if int(n) % s == 0 else 'No')


if __name__ == "__main__":
    # execute only if run as a script
    main()
