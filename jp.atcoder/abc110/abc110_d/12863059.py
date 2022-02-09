import sys

MOD = 10 ** 9 + 7
# MOD = 998244353
def make_tables(n=10 ** 9, r=2 * 10 ** 6, p=MOD):
  fac = [None] * (r + 1); fac[0] = 1
  for i in range(r): fac[i+1] = fac[i] * (i + 1) % p
  ifac = [None] * (r + 1); ifac[r] = pow(fac[r], p - 2, p)
  for i in range(r, 0, -1): ifac[i-1] = ifac[i] * i % p
  n_choose = [None] * (r + 1); n_choose[0] = 1
  for i in range(r): n_choose[i+1] = n_choose[i] * (n - i) % p
  for i in range(r + 1): n_choose[i] = n_choose[i] * ifac[i] % p
  return fac, ifac, n_choose

fac, ifac, n_choose = make_tables()

def mod_choose(n, r, p=MOD):
  if r > n or r < 0: return 0
  return fac[n] * ifac[r] % p * ifac[n-r] % p

def nHr(n, r, p=MOD):
  return fac[n-1+r] * ifac[n-1] % p * ifac[r] % p

def sieve_of_eratosthenes(n=10 ** 6):
  sieve = [1] * (n + 1); sieve[0] = sieve[1] = 0
  for i in range(2, int(n ** 0.5) + 1):
    if not sieve[i]: continue
    for j in range(i * 2, n + 1, i): sieve[j] = 0
  prime_numbers = [i for i in range(2, n + 1) if sieve[i]]
  return sieve, prime_numbers

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

n, m = map(int, sys.stdin.readline().split())

def main():
  res = 1
  for p, c in prime_factorize(m).items():
    res *= nHr(n, c)
    res %= MOD
  print(res)

if __name__ == '__main__':
  main()
