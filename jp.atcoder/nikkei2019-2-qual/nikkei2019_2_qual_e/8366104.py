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
    n, k = (int(x) for x in sys.stdin.readline().split())
    if n - 2 * k + 1 >= 0:
        # 存在する
        print(k, 2 * n, k + 2 * n)


    else:
        print(-1)



if __name__ == "__main__":
    # execute only if run as a script
    main()
