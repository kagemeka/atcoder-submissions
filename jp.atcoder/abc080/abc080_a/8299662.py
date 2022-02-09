import sys
read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    a, t, b = (int(x) for x in read().split())
    if a * t >= b: print(b)
    else: print(a * t)


if __name__ == "__main__":
    # execute only if run as a script
    main()
