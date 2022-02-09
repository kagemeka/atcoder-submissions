import sys
import itertools

# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics


# bit を使ってci を管理する

def toBit(n):
    return eval('0b' + n)

def main():

    n = int(sys.stdin.readline().rstrip())

    schedule = [toBit(''.join(str(x) for x in sys.stdin.readline().split())) for _ in range(n)]
    profit_table = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]

    maximum_profit = -10**10
    for open_pattern in itertools.product('01', repeat=10):
        open_pattern = toBit(''.join(open_pattern))
        if open_pattern == '0b0':
            continue
        profit = 0
        for i in range(n):
            checked = schedule[i]
            number_of_periods = bin(checked & open_pattern).count('1')
            profit += profit_table[i][number_of_periods]
        maximum_profit = max(maximum_profit, profit)

    print(maximum_profit)

if __name__ == "__main__":
    # execute only if run as a script
    main()
