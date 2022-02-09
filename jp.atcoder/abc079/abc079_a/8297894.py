import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n = sys.stdin.readline().rstrip()

    count = 1
    for i in range(len(n)-1):
        if n[i] == n[i+1]: count += 1

    print('Yes' if count >= 3 else 'No')


if __name__ == "__main__":
    # execute only if run as a script
    main()
