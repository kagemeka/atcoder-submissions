#                         author:  kagemeka
#                         created: 2019-11-08 23:31:18(JST)
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
    n, y = (int(i) for i in sys.stdin.readline().split())
    y //= 1000

    if 10 * n < y or n > y:
        print(-1, -1, -1)
        exit()

    for i in range(y // 10 + 1):
        for j in range((y - i * 10) // 5 + 1):
            k = n - (i + j)
            if 10 * i + 5 * j + k == y:
                print(i, j, k)
                exit()

    print(-1, -1, -1)

if __name__ == "__main__":
    # execute only if run as a script
    main()
