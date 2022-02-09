#                         author:  kagemeka
#                         created: 2019-11-09 15:46:24(JST)
### modules
## from standard library
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
## from external libraries
# import scipy.special
# import scipy.misc
# import numpy as np
def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def main():
    n = int(sys.stdin.readline().rstrip())

    count = 0
    for i in range(1, n + 1, 2):
        if len(divisors(i)) == 8:
            count += 1

    print(count)




if __name__ == "__main__":
    # execute only if run as a script
    main()
