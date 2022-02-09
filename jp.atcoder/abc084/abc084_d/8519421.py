import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def primeNums(n):
    from math import floor, sqrt
    sieve = set(range(2, n + 1))
    if 2 in sieve:
        not_prime = set(range(2 * 2, n + 1, 2))
        sieve -= not_prime
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if i in sieve:
            not_prime = set(range(i * 2, n + 1, i))
            sieve -= not_prime
    return sieve

limit = 10 ** 5
prime_table = [0 for _ in range(limit + 1)]
for p in primeNums(limit):
    prime_table[p] = 1

def main():

    q = int(sys.stdin.readline().rstrip())
    lines = sys.stdin.readlines()

    for j in range(q):
        l, r = [int(x) for x in lines[j].split()]
        res = 0
        for i in range(l if l % 2 == 1 else l + 1, r + 1, 2):
            res += (prime_table[(i + 1) // 2] if prime_table[i] else 0)

        print(res)


if __name__ == "__main__":
    # execute only if run as a script
    main()
