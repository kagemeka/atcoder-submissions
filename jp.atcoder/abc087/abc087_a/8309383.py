#                         author:  kagemeka
#                         created: 2019-11-06 14:53:37(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    x, a, b = (int(i) for i in sys.stdin.read().split())
    ans = (x - a) % b
    print(ans)



if __name__ == "__main__":
    # execute only if run as a script
    main()
