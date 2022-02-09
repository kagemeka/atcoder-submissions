import sys
# import collections
# import math
# import bisect
# import re
# import itertools


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

like_2017_table = [0 for _ in range(limit + 1)]
for i in range(3, limit + 1, 2):
    if prime_table[i] and prime_table[(i + 1) // 2]:
            like_2017_table[i] = 1

s = [0 for _ in range(limit + 1)]
for i in range(limit):
    s[i+1] = s[i] + like_2017_table[i+1]

def main():

    q = int(sys.stdin.readline().rstrip())
    m = map(int, sys.stdin.read().split())

    for l, r in zip(m, m):
        res = s[r] - s[l-1]
        print(res)


if __name__ == "__main__":
    main()
