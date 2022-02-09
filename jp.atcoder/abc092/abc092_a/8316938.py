#                         author:  kagemeka
#                         created: 2019-11-07 00:57:57(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator

def main():
    a, b, c, d = (int(x) for x in sys.stdin.read().split())
    train_fare = a if a <= b else b
    bus_fare = c if c <= d else d
    print(train_fare + bus_fare)



if __name__ == "__main__":
    # execute only if run as a script
    main()
