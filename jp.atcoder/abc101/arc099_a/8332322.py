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
    n, k, *a = (int(x) for x in sys.stdin.read().split())
    i = a.index(1)
    left, right = i, (n - 1) - i
    if left % 2 == 0:
        if right % 2 == 0:
            ans = left // 2 + right // 2
        else:
            ans = left // 2 + right // 2 + 1
    else:
        ans = left // 2 + right // 2 + 1

    print(ans)




if __name__ == "__main__":
    # execute only if run as a script
    main()
