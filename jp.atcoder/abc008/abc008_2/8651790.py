# 2019-11-25 22:51:53(JST)
import sys
from collections import Counter
from operator import itemgetter


def main():
    n, *cand = sys.stdin.read().split()

    res = sorted((vote, cand)for cand, vote in Counter(cand).items())

    print(res[-1][1])

if __name__ == '__main__':
    main()
