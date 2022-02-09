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
    n, k = (int(x) for x in sys.stdin.readline().split())
    print(0 if n % k == 0 else 1)



if __name__ == "__main__":
    # execute only if run as a script
    main()
