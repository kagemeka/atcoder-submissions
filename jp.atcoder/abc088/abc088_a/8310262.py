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
    n, a = (int(x) for x in sys.stdin.read().split())
    print('Yes' if n % 500 <= a else 'No')


if __name__ == "__main__":
    # execute only if run as a script
    main()
