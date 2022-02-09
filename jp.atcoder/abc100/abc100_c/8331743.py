#                         author:  kagemeka
#                         created: 2019-11-08 12:38:16(JST)
## internal modules
import sys
# import collections
import math
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
    n, *a = (int(x) for x in sys.stdin.read().split())

    total_count = 0
    atmost = math.floor(math.log(10 ** 9, 2))
    for i in range(n):
        current = a[i]
        count = 0
        for _ in range(atmost + 1):
            if current % 2 == 0:
                current //= 2
                count += 1
            else:
                break
        total_count += count

    print(total_count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
