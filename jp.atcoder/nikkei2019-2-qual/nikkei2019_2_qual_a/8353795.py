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
    if n % 2 == 0:
        ans = n // 2 - 1
    else:
        ans = n // 2
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
