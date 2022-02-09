#                         author:  kagemeka
#                         created: 2019-11-09 15:46:24(JST)
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
    a, b = (int(x) for x in sys.stdin.readline().split())
    area = a * b - (a + b - 1)
    print(area)



if __name__ == "__main__":
    # execute only if run as a script
    main()
