import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n = sys.stdin.readline().rstrip()

    if n[0] * 3 in n: ans = 'Yes'
    elif n [3] * 3 in n: ans = 'Yes'
    else: ans = 'No'
    print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
