import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    xy = sys.stdin.read().split()
    if xy[0] == xy[1]: print('=')
    else:
        if xy == sorted(xy): print('<')
        else: print('>')


if __name__ == "__main__":
    # execute only if run as a script
    main()
