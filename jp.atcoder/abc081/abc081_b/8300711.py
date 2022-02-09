import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, *numbers = (int(x) for x in sys.stdin.read().split())
    still_can_be_divided = True
    count = 0
    while still_can_be_divided:
        for i in range(n):
            if numbers[i] % 2 == 0:
                numbers[i] //= 2
            else:
                still_can_be_divided = False
        if still_can_be_divided:
            count += 1

    print(count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
