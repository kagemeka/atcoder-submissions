import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, a, b = (int(x) for x in sys.stdin.read().split())
    total = 0
    for i in range(1, n+1):
        s = sum(list(int(x) for x in str(i)))
        if a <= s <= b: total += i
    print(total)

if __name__ == "__main__":
    # execute only if run as a script
    main()
