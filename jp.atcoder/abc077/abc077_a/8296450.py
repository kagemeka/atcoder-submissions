
import sys
# import collections
# import math
# import string
# import bisect

def main():
    c1, c2 = sys.stdin.read().split()
    print('YES' if c1 == c2[::-1] else 'NO')

if __name__ == "__main__":
    main()
