#                         author:  kagemeka
#                         created: 2019-11-06 12:47:30(JST)
import sys
# import collections
import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    ab = sys.stdin.readline().split()
    n = int(''.join(ab))
    print('Yes' if math.floor(n ** 0.5) ** 2 == n else 'No')


if __name__ == "__main__":
    # execute only if run as a script
    main()
