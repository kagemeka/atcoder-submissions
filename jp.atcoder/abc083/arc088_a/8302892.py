import sys
# import collections
import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    x, y = (int(i) for i in sys.stdin.read().split())
    ans = 1 + math.floor(math.log2(y / x))
    print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
