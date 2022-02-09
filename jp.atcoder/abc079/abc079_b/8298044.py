import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n = int(sys.stdin.readline().rstrip())
    l = [None] * (n + 1); l[0], l[1] = 2, 1
    for i in range(1, n):
        l[i+1] = l[i] + l[i-1]
    print(l[n])

if __name__ == "__main__":
    # execute only if run as a script
    main()
