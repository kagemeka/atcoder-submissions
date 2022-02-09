#                         author:  kagemeka
#                         created: 2019-11-07 13:42:36(JST)
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
    k = int(sys.stdin.readline().rstrip())
    n = len(s)

    substrings = []
    for i in range(1, k+1):
        for j in range(n-i+1):
            substring = s[j:j+i]
            substrings.append(substring)
    substrings = sorted(list(set(substrings)))
    print(substrings[k-1])


if __name__ == "__main__":
    # execute only if run as a script
    main()
