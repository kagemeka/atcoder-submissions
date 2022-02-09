#                         author:  kagemeka
#                         created: 2019-11-06 16:52:04(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, *s = sys.stdin.read().split()
    l = len(set(s))
    if l == 3: ans = 'Three'
    else: ans = 'Four'
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
