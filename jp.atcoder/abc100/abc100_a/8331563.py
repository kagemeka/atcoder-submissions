#                         author:  kagemeka
#                         created: 2019-11-08 12:38:16(JST)
## internal modules
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
## external modules
# import scipy.special   # if use comb function on AtCoder,
# import scipy.misc      # select scipy.misc.comb (old version)

def main():
    a, b = (int(x) for x in sys.stdin.readline().split())
    if abs(a - b) <= 1:
        ans = 'Yay!'
    else:
        more_eat = max(a, b) - (min(a, b) + 1)
        remainder = 16 - (min(a, b) * 2 + 1)

        if more_eat <= remainder // 2:
            ans = 'Yay!'
        else:
            ans = ':('

    print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
