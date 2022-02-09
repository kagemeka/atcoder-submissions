#                         author:  kagemeka
#                         created: 2019-11-08 23:31:18(JST)
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
# import scipy.special
# import scipy.misc
# import numpy as np

def main():

    k, s = (int(i) for i in sys.stdin.readline().split())

    count = 0
    for x in range(k + 1):
        if 0 <= s - x <= k:
            count += s - x  + 1
        elif k < s - x <= 2 * k:
            count += k - (s - x - k) + 1


    print(count)


if __name__ == "__main__":
    # execute only if run as a script
    main()
