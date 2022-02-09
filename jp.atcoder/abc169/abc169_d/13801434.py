import sys

import numpy as np
def sieve_of_eratosthenes(n=10**6):
  sieve = np.ones(n+1); sieve[:2] = 0
  for i in range(2, int(n**.5)+1):
    if sieve[i]: sieve[i*2::i] = 0
  return sieve, np.flatnonzero(sieve)

# def sieve_of_eratosthenes(n=10**6):
#   sieve = [1] * (n+1); sieve[0] = sieve[1] = 0
#   for i in range(2, int(n**.5)+1):
#     if not sieve[i]: continue
#     for j in range(i*2, n+1, i): sieve[j] = 0
#   prime_nums = [i for i in range(2, n+1) if sieve[i]]
#   return sieve, prime_nums

is_prime, prime_nums = sieve_of_eratosthenes()

def prime_factorize(n):
  res = dict()
  if n < 2: return res
  border = int(n**.5)
  for p in prime_nums:
    if p > border: break
    while n % p == 0: res[p] = res.get(p, 0)+1; n //= p
    if n == 1: return res
  res[n] = 1
  return res

def prime_factorize_fac(n):
  res = dict()
  for i in range(2, n+1):
    for p, c in prime_factorize(i).items(): res[p] = res.get(p, 0)+c
  return res

def main():
    n = int(sys.stdin.readline().rstrip())
    res = prime_factorize(n)
    ans = 0
    for m in res.values():
        i = 1
        while True:
            if (1 + i) * i // 2 > m:
                i -= 1
                break
            i += 1
        ans += i
    print(ans)




if __name__ == '__main__':
    main()
