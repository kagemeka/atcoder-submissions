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

def main():
    *n, = (int(x) for x in sys.stdin.readline().split())
    n.sort()
    print(n[-1] - n[0])


if __name__ == "__main__":
    # execute only if run as a script
    main()
