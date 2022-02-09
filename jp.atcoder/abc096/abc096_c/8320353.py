#                         author:  kagemeka
#                         created: 2019-11-07 13:09:56(JST)
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
    h, w = (int(x) for x in sys.stdin.readline().split())
    canvas = ['.' * (w + 2)]
    for i in range(h):
        line = '.' + sys.stdin.readline().rstrip() + '.'
        canvas.append(line)
    canvas.append('.' * (w + 2))
    for i in range(1, h+1):
        for j in range(1, w+1):
            if canvas[i][j] == '.':
                continue
            else:
                if canvas[i-1][j] == '#' or canvas[i][j-1] == '#' or canvas[i][j+1] == '#' or canvas[i+1][j] == '#':
                    continue
                else:
                    print('No')
                    exit()
    print('Yes')


if __name__ == "__main__":
    # execute only if run as a script
    main()
