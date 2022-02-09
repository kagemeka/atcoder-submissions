#                         author:  kagemeka
#                         created: 2019-11-06 22:04:18(JST)
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

def main():
    a, b, c = (int(x) for x in sys.stdin.read().split())
    if c <= a + b:
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)



if __name__ == "__main__":
    # execute only if run as a script
    main()
