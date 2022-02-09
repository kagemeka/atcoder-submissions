#                         author:  kagemeka
#                         created: 2019-11-09 21:20:16(JST)
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
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]

    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]:
            print('No')
            exit()
    print('Yes')


if __name__ == "__main__":
    # execute only if run as a script
    main()
