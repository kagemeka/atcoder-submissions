#                         author:  kagemeka
#                         created: 2019-11-06 22:04:18(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator

def main():
    n = int(sys.stdin.readline().rstrip())
    red = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    blue = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    reversed_b_sorted_by_a= [ab[1] for ab in sorted(red, reverse=1)]
    bd_sorted_by_ac = [acbd[1] for acbd in sorted(red + blue)]


    count = 0
    for b in reversed_b_sorted_by_a:
        b_index = bd_sorted_by_ac.index(b)
        if b_index == len(bd_sorted_by_ac) - 1:
            bd_sorted_by_ac.remove(b)
            continue

        range_to_scope = bd_sorted_by_ac[b_index+1:]
        possible_elements = [x for x in range_to_scope if x > b]
        if not possible_elements:
            bd_sorted_by_ac.remove(b)
            continue

        bd_sorted_by_ac.remove(min(possible_elements))
        bd_sorted_by_ac.remove(b)
        count += 1
    print(count)


if __name__ == "__main__":
    # execute only if run as a script
    main()
