import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    x, y, z = (int(i) for i in sys.stdin.read().split())
    n = 0
    while True:
        total = (n + 1) * z + n * y
        if total <= x: n += 1; continue
        else:
            if n == 0: print(0)
            else:print(n-1)
            exit()

if __name__ == "__main__":
    # execute only if run as a script
    main()
