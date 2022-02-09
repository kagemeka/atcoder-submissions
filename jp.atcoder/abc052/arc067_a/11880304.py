import sys

import numpy as np
def sieve_of_eratosthenes(n=10 ** 7):
  sieve = np.ones(n + 1); sieve[:2] = 0
  for i in range(2, int(np.sqrt(n)) + 1):
    if sieve[i]: sieve[i*2::i] = 0
  return sieve, np.flatnonzero(sieve)

is_prime, prime_numbers = sieve_of_eratosthenes()

def prime_factorize(n):
  res = dict()
  if n < 2: return res
  border = int(n ** 0.5)
  for p in prime_numbers:
    if p > border: break
    while n % p == 0: res[p] = res.get(p, 0) + 1; n //= p
    if n == 1: return res
  res[n] = 1
  return res

def prime_factorize_factorial(n):
  res = dict()
  for i in range(2, n + 1):
    for p, c in prime_factorize(i).items(): res[p] = res.get(p, 0) + c
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
