#                         author:  kagemeka
#                         created: 2019-11-10 12:28:14(JST)
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
    if (a * b) % 2 !- 0:
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
