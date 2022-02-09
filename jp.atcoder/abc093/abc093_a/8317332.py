#                         author:  kagemeka
#                         created: 2019-11-07 02:35:07(JST)
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
    s = sys.stdin.readline().rstrip()
    print('Yes' if len(set(s)) == 3 else 'No')


if __name__ == "__main__":
    # execute only if run as a script
    main()
