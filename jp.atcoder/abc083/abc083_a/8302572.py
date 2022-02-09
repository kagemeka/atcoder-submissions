import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    a, b, c, d = (int(x) for x in sys.stdin.read().split())
    left = a + b
    right = c + d
    if left > right: ans = "Left"
    elif right > left: ans = 'Right'
    else: ans = 'Balanced'
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
