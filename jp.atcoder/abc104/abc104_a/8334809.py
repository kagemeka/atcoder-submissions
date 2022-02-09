#                         author:  kagemeka
#                         created: 2019-11-08 18:39:24(JST)
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
# imort numpy as np

def main():
    r = int(sys.stdin.readline().rstrip())
    if r < 1200:
        ans = 'ABC'
    elif r < 2800:
        ans = 'ARC'
    else:
        ans = 'AGC'

    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
