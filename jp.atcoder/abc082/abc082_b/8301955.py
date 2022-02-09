import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    s, t = sys.stdin.read().split()
    n, m = len(s), len(t)
    s = sorted(s)
    t = list(reversed(sorted(t)))
    if n < m:
        for i in range(n):
            if s[i] < t[i]: ans = 'Yes'; break
            elif s[i] > t[i]: ans = 'No'; break
        else:
            ans = 'Yes'
    else:
        for i in range(m):
            if s[i] < t[i]: ans = 'Yes'; break
            elif s[i] > t[i]: ans = 'No'; break
        else:
            ans = 'No'

    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
