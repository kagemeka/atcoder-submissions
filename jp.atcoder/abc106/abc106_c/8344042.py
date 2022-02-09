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
    s = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline().rstrip())

    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
        else:
            last_1 = i - 1
            break
    else:
        last_1 = len(s) - 1

    if k <= count:
        ans = '1'
    else:
        ans = s[last_1 + 1]

    print(ans)




if __name__ == "__main__":
    # execute only if run as a script
    main()
