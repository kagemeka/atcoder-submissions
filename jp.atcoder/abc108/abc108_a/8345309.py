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
    k = int(sys.stdin.readline().rstrip())
    if k % 2 == 0:
        e_c, o_c = k // 2, k // 2
    else:
        e_c, o_c = k // 2, k // 2 + 1

    ans = e_c * o_c
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
