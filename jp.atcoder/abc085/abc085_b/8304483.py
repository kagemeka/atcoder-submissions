import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, *d = (int(x) for x in sys.stdin.read().split())
    print(len(set(d)))


if __name__ == "__main__":
    # execute only if run as a script
    main()
