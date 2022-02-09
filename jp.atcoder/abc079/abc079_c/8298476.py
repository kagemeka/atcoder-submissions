import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    a, b, c, d = (int(x) for x in list(sys.stdin.readline().rstrip()))
    s = 7 - a
    if sum([b, c, d]) == s: res = '+++'
    elif sum([-b, c, d]) == s: res = '-++'
    elif sum([b, -c, d]) == s: res = '+-+'
    elif sum([b, c, -d]) == s: res = '++-'
    elif sum([-b, -c, d]) == s: res = '--+'
    elif sum([-b, c, -d]) == s: res = '-+-'
    elif sum([b, -c, -d]) == s: res = '+--'
    if res[0] == '-': b = -b
    if res[1] == '-': c = -c
    if res[2] == '-': d = -d
    ans = [str(a)]
    for x in [b, c, d]:
        if x >= 0 : x = '+' + str(x)
        else: x = str(x)
        ans.append(x)
    print(''.join(ans) + '=7')


if __name__ == "__main__":
    # execute only if run as a script
    main()
