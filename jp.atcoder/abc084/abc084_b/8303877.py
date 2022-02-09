import sys
# import collections
# import math
import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    a, b = (int(x) for x in sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip()
    if s[a] == '-':
        s_a, s_b = s[:a], s[a+1:]
        for i in s_a:
            if not i in string.digits:
                f_a = False
                break
        else:
            f_a = True
            for i in s_b:
                if not i in string.digits:
                    f_b = False
                    break
            else:
                f_b = True
    else:
        print('No')
        exit()

    print('Yes' if f_a and f_b else 'No')

if __name__ == "__main__":
    # execute only if run as a script
    main()
