#                         author:  kagemeka
#                         created: 2019-11-08 02:12:52(JST)
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
    n = int(sys.stdin.readline().rstrip())
    count = 0
    for _ in range(n):
        if n < 6:
            count += n
            break
        elif n >= 15 or 12 > n >= 6:
            n -= max(6 ** math.floor(math.log(n, 6)), 9 ** math.floor(math.log(n, 9)))
            count += 1
        elif 15 > n >= 12:
            n -= 6
            count += 1

        print(n)
    print(count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
