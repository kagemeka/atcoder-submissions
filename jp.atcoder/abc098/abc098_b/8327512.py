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
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()

    max_count = 0
    for i in range(1, n):
        s1, s2 = s[:i], s[i:]
        count = 0
        for l in set(s1):
            if l in s2:
                count += 1
        max_count = max(count, max_count)

    print(max_count)





if __name__ == "__main__":
    # execute only if run as a script
    main()
