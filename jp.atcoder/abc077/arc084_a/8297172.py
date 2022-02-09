
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
        for b, cb in collections.Counter((b for b in middles if b > a)).items():
            count += ca * cb * len([c for c in lowers if c > b])

    print(count)

if __name__ == "__main__":
    main()
