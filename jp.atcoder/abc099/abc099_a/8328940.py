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
    n = int(sys.stdin.readline().rstrip())
    if n < 1000:
        ans = 'ABC'
    else:
        ans = 'ABD'

    print(ans)



if __name__ == "__main__":
    # execute only if run as a script
    main()
