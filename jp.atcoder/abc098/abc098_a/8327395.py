#                         author:  kagemeka
#                         created: 2019-11-07 23:33:56(JST)
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
    ans = max(a + b, a - b, a * b)
    print(ans)



if __name__ == "__main__":
    # execute only if run as a script
    main()
