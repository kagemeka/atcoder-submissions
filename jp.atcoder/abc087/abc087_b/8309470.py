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
    a, b, c, x = (int(i) for i in sys.stdin.read().split())

    combination = 0
    for i in range(a+1):
        ta = 500 * i
        if ta == x:
            combination += 1
            continue
        elif ta> x:
            continue
        for j in range(b+1):
            tb = 100 * j
            if ta + tb == x:
                combination += 1
                continue
            elif ta + tb > x:
                continue
            for k in range(c+1):
                total = ta + tb + 50 * k
                if total == x:
                    combination += 1

    print(combination)

if __name__ == "__main__":
    # execute only if run as a script
    main()
