#                         author:  kagemeka
#                         created: 2019-11-06 21:30:22(JST)
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
    s = [sys.stdin.readline().rstrip() for _ in range(3)]
    ans = ''.join([s[i][i] for i in range(3)])
    print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
