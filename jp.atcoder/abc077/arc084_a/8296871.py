
import sys
import collections
# import math
# import string
# import bisect

def main():
    n, *parts = (int(x) for x in sys.stdin.read().split())
    uppers, middles, lowers = (parts[n*i:n*(i+1)] for i in range(3))

    count = 0
    for a, ca in collections.Counter(uppers).items():
        for b, cb in collections.Counter(middles).items():
            if a >= b: continue
            else:
                for c, cc in collections.Counter(lowers).items():
                    if b >= c: continue
                    else: count += ca * cb * cc
    print(count)

if __name__ == "__main__":
    main()
