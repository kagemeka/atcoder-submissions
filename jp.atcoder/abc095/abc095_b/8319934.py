#                         author:  kagemeka
#                         created: 2019-11-07 12:33:44(JST)
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
    n, x, *m = (int(i) for i in sys.stdin.read().split())
    x -= sum(m)
    c = n
    c += x // min(m)
    print(c)



if __name__ == "__main__":
    # execute only if run as a script
    main()
