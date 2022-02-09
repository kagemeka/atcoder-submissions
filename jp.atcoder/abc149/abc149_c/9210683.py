import sys
from math import floor, sqrt
from bisect import bisect_left as bi_l

def prime_nums(n):
    sieve = set(range(2, n + 1))
    non_prime = set(range(2 * 2, n + 1, 2))
    sieve -= non_prime
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if i in sieve:
            non_prime = set(range(i * 2, n + 1, i))
            sieve -= non_prime
    return sieve

ps = prime_nums(10 ** 6)
ps = sorted(ps)

x = int(sys.stdin.readline().rstrip())

def main():
    return ps[bi_l(ps, x)]

if __name__ == '__main__':
    ans = main()
    print(ans)
