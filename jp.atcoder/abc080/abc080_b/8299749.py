import sys
# read = sys.stdin.read
readline = sys.stdin.readline
# readlines = sys.stdin.readlines
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n = readline().rstrip()
    digits = [int(d) for d in n]
    print('Yes' if int(n) % sum(digits) == 0 else 'No')

if __name__ == "__main__":
    # execute only if run as a script
    main()
