#                         author:  kagemeka
#                         created: 2019-11-08 14:51:29(JST)
## internal modules
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
## external modules
# import scipy.special   # if use comb function on AtCoder,
# import scipy.misc      # select scipy.misc.comb (old version)

def main():
    n, *a = (int(x) for x in sys.stdin.read().split())

    for i in range(n):
        a[i] -= (i + 1)

    b1 = math.floor(sum(a) / n)
    b2 = math.ceil(sum(a) / n)

    ans = min(sum([abs(a[i] - b1) for i in range(n)]), sum([abs(a[i] - b2) for i in range(n)]))
    print(ans)



if __name__ == "__main__":
    # execute only if run as a script
    main()
