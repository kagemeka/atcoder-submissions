#                         author:  kagemeka
#                         created: 2019-11-07 11:52:43(JST)
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
    n, *x = (int(i) for i in sys.stdin.read().split())
    s_x = list(sorted(x))
    half = n // 2
    m_s, m_l = s_x[half - 1], s_x[half]
    for i in x:
        print(m_l if i < m_l else m_s)

if __name__ == "__main__":
    # execute only if run as a script
    main()
