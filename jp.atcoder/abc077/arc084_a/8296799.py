
import sys
# import collections
# import math
# import string
# import bisect

def main():
    n, *parts = (int(x) for x in sys.stdin.read().split())
    uppers, middles, lowers = (sorted(parts[n*i:n*(i+1)], reverse=1) for i in range(3))

    count = 0
    for a in uppers:
        for b in middles:
            if a >= b: break
            else:
                for c in lowers:
                    if b >= c: break
                    else: count += 1
    print(count)

if __name__ == "__main__":
    main()
