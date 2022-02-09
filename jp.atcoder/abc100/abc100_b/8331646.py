#                         author:  kagemeka
#                         created: 2019-11-08 12:38:16(JST)
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
    d, n = (int(x) for x in sys.stdin.readline().split())
    if n < 100:
        ans = n * 100 * d
    else:
        ans = 101 * 100 * d

    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
