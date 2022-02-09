#                         author:  kagemeka
#                         created: 2019-11-09 16:39:51(JST)
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
    n, i = (int(x) for x in sys.stdin.readline().split())
    j = n - i + 1
    print(j)


if __name__ == "__main__":
    # execute only if run as a script
    main()
