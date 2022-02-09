
import sys
# import collections
# import math
# import string
import bisect

def main():
    n, *parts = (int(x) for x in sys.stdin.read().split())
    uppers, middles, lowers = (parts[n*i:n*(i+1)] for i in range(3))
    uppers.sort()
    lowers.sort()

    count = 0
    for j in middles:
        i = bisect.bisect_left(uppers, j)
        k = len(lowers) - bisect.bisect_right(lowers, j)
        count += i * k

    print(count)

if __name__ == "__main__":
    main()
