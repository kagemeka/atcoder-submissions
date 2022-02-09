#                         author:  kagemeka
#                         created: 2019-11-06 12:47:30(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    a, b = (int(x) for x in sys.stdin.readline().split())
    print('Even' if a * b % 2 == 0 else 'Odd')

if __name__ == "__main__":
    # execute only if run as a script
    main()
