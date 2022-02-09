import sys
from collections import defaultdict
from bisect import bisect_right as bi_r

U = 2 * 10 ** 6
def sieve_of_eratosthenes(n=U):
  if n == 1: return set()
  sieve = set(range(2, n + 1))
  for p in sieve_of_eratosthenes(int(n ** 0.5)):
    sieve -= set(range(p * 2, n + 1, p))
  return sieve

prime_numbers = sieve_of_eratosthenes()
soted_prime_numbers = sorted(prime_numbers)

def is_prime(n): return n in prime_numbers

def prime_factorize(n):
  res = defaultdict(int)
  if n < 2: return res
  for p in soted_prime_numbers[:bi_r(soted_prime_numbers, int(n ** 0.5))]:
    while n % p == 0:
      res[p] += 1
      n //= p
    if n == 1:
      return res
  res[n] = 1
  return res

def prime_factorize_factorial(n):
  res = defaultdict(int)
  for i in range(2, n + 1):
    for p, c in prime_factorize(i).items():
      res[p] += c
  return res

MOD = 10 ** 9 + 7

n = int(sys.stdin.readline().rstrip())

def main():
    res = 1
    for c in prime_factorize_factorial(n).values():
        res *= c + 1; res %= MOD
    print(res)

if __name__ ==  '__main__':
    main()
