import sys
# import collections
# import math
import string
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
            f_s, f_t = False, False
            for c in string.ascii_lowercase:
                if s[i] == c: f_s = True
                if t[i] == c: f_t = True

                if f_s and not f_t: print('Yes'); exit()
                elif not f_s and f_t: print('No'); exit()
                elif f_s and f_t: break
                else: continue
        ans = 'Yes'
    else:
        for i in range(m):
            for c in string.ascii_lowercase:
                f_s, f_t = False, False
                if s[i] == c: f_s = True
                if t[i] == c: f_t = True

                if f_s and not f_t: print('Yes'); exit()
                elif not f_s and f_t: print('No'); exit()
                elif f_s and f_t: break
                else: continue
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
