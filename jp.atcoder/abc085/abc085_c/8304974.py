import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, y = (int(i) for i in sys.stdin.readline().split())
    y //= 1000
    if y > 10 * n or y < n: print('-1 -1 -1'); exit()

    for i in range(n+1):
        for j in range(n+1-i):
            k = n - i - j
            t = 10 * i + 5 * j + k
            if t == y:
                print(i, j, k)
                exit()
    print(-1, -1, -1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
