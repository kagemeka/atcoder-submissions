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
    h, w = (int(x) for x in sys.stdin.readline().split())
    a = [list(sys.stdin.readline().rstrip()) for _ in range(h)]

    for i in range(len(a)-1, -1, -1):
        for j in range(len(a[0])-1, -1, -1):
            if a[i][j] == '#':
                break
        else:
            del a[i]

    for j in range(len(a[0])-1, -1, -1):
        for i in range(len(a)-1, -1, -1):
            if a[i][j] == '#':
                break
        else:
            for i in range(len(a)-1, -1, -1):
                del a[i][j]

    for i in range(len(a)):
        print(''.join(a[i]))



if __name__ == "__main__":
    # execute only if run as a script
    main()
