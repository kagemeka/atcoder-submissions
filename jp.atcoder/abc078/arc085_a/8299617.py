import sys
read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, m = (int(x) for x in read().split())
    ans = (1900 * m + 100 *(n - m)) * 2 ** m
    print(ans)
    # editorialカンニングした
    # m個TLEがあるとき、次に提出したときにそれらがすべてACとなる確率は(1/2)**m
    # 確率の期待値が1になる実行回数は逆数で2**mってこと？
    # 本当ならlimitを計算すべきなんだろうが...

if __name__ == "__main__":
    # execute only if run as a script
    main()
