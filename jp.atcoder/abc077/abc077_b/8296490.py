
import sys
# import collections
import math
# import string
# import bisect

def main():
    n = int(sys.stdin.readline().rstrip())
    ans = math.floor(n ** 0.5) ** 2
    print(ans)

if __name__ == "__main__":
    main()
