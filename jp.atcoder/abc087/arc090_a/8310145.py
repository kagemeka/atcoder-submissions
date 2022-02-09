#                         author:  kagemeka
#                         created: 2019-11-06 14:53:37(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, a, b = (x for x in sys.stdin.readlines())
    n = int(n.rstrip())
    a = [int(x) for x in a.split()]
    b = [int(x) for x in b.split()]

    total = a[0] + b[-1]
    sa, sb = sum(a[1:]), sum(b[:-1])
    for i in range(n-1):
        if sa >= sb:
            total += a[i+1]
            sa -= a[i+1]
            sb -= b[i]
        else:
            for j in range(i+1, n-1):
                if sum(a[i+1:j+1]) - sum(b[i:j]) >= 0:
                    total += a[i+1]
                    sa -= a[i+1]
                    sb -= b[i]
                    break
                else:
                    continue
            else:
                total += sb
                break
    print(total)


if __name__ == "__main__":
    # execute only if run as a script
    main()
