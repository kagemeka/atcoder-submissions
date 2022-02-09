#                         author:  kagemeka
#                         created: 2019-11-09 11:51:37(JST)
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
    n = int(sys.stdin.readline().rstrip())

    for x in range(n // 7 + 1):
        if (n - 7 * x) % 4 == 0:
            print('Yes')
            exit()
    print('No')


if __name__ == "__main__":
    # execute only if run as a script
    main()
