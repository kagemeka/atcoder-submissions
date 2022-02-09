#                         author:  kagemeka
#                         created: 2019-11-08 02:12:52(JST)
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
    a, b = (int(x) for x in sys.stdin.readline().split())
    diff = b - a
    altitude = (1 + diff - 1) * (diff - 1) // 2 - a
    print(altitude)



if __name__ == "__main__":
    # execute only if run as a script
    main()
