#                         author:  kagemeka
#                         created: 2019-11-07 11:52:43(JST)
import sys
# import collections
# import math
# import string
import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator

def main():
    n, *x = (int(i) for i in sys.stdin.read().split())
    s_x = list(sorted(x))
    m_s, m_l = s_x[n // 2 -1], s_x[n // 2]
    for i in x:
        b = bisect.bisect_left(s_x, i)
        print(m_l if b < n // 2 else m_s)

if __name__ == "__main__":
    # execute only if run as a script
    main()
