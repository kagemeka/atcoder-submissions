import sys
# import collections
import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    a, b = (int(x) for x in sys.stdin.readline().split())
    ans = math.ceil((a + b) / 2)
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
