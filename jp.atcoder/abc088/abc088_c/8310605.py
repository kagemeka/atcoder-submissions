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
    c = [[int(x) for x in sys.stdin.readline().split()] for _ in range(3)]
    n = 3  # able to deal with n x n
    d = []
    for i in range(1, n):
        d0i = c[0][i] - c[0][0]
        d.append(d0i)
    for i in range(1,n):
        for j in range(1, n):
            if c[i][j] - c[i][0] == d[j-1]:
                continue
            else:
                print('No')
                exit()
    print('Yes')

if __name__ == "__main__":
    # execute only if run as a script
    main()
