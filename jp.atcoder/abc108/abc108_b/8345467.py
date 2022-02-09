#                         author:  kagemeka
#                         created: 2019-11-09 18:08:09(JST)
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
    x1, y1, x2, y2 = (int(i) for i in sys.stdin.readline().split())

    x3 = x2 + (y1 - y2)
    x4 = x1 + (y1 - y2)
    y3 = y2 - (x1 - x2)
    y4 = y1 - (x1 - x2)

    print(x3, y3, x4, y4)


if __name__ == "__main__":
    # execute only if run as a script
    main()
