#                         author:  kagemeka
#                         created: 2019-11-08 18:39:24(JST)
### modules
## from standard library
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
## from external libraries
# import scipy.special   # if use comb function on AtCoder,
# import scipy.misc      # select scipy.misc.comb (old version)
# imort numpy as np

def main():
    s = sys.stdin.readline().rstrip()

    if s[0] == 'A':
        s = s[1:]
        if 'C' in s[1:-1] and s.count('C') == 1:
            s = s.replace('C', 'a')
            if s.lower() == s:
                print('AC')
                exit()

    print('WA')

if __name__ == "__main__":
    # execute only if run as a script
    main()
