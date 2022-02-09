#                         author:  kagemeka
#                         created: 2019-11-07 23:33:56(JST)
## internal modules
import sys
import collections
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

    opposite = collections.Counter(s)
    opposite['W'] = 0
    minimum = n
    for i in range(n):
        if s[i] == 'E':
            opposite['E'] -= 1
        minimum = min(minimum, sum(opposite.values()))
        if s[i] == 'W':
            opposite['W'] += 1
    print(minimum)




if __name__ == "__main__":
    # execute only if run as a script
    main()
