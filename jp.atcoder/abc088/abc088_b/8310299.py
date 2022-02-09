#                         author:  kagemeka
#                         created: 2019-11-06 16:18:30(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, *a = (int(x) for x in sys.stdin.read().split())
    a.sort(reverse=1)
    alice, bob = 0, 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    ans = alice - bob
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
