import sys

import numpy as np
MOD = 10 ** 9 + 7
def cumprod(a, p):
  l = len(a); sql = int(np.sqrt(l) + 1)
  a = np.resize(a, sql ** 2).reshape(sql, sql)
  for i in range(sql - 1): a[:, i+1] *= a[:, i]; a[:, i+1] %= p
  for i in range(sql - 1): a[i+1] *= a[i, -1]; a[i+1] %= p
  return np.ravel(a)[:l]

def make_tables(n=10 ** 9, r=5 * 10 ** 6, p=MOD):
  fac = np.arange(r + 1); fac[0] = 1; fac = cumprod(fac, p)
  ifac = np.arange(r + 1, 0, -1); ifac[0] = pow(int(fac[-1]), p - 2, p)
  ifac = cumprod(ifac, p)[n::-1]
  n_choose = np.arange(n + 1, n - r, -1); n_choose[0] = 1;
  n_choose[1:] = cumprod(n_choose[1:], p) * ifac[1:r+1] % p
  return fac, ifac, n_choose

fac, ifac, n_choose = make_tables(r=10**5)

def choose(n, r, p=MOD):
  if r > n or r < 0: return 0
  return fac[n] * ifac[r] % p * ifac[n-r] % p

n, k, *a = map(int, sys.stdin.read().split())
a.sort()

def main():
  res = 0
  for i in range(n):
    res += choose(i, k - 1) * a[i] % MOD
    res -= choose(n - i - 1, k - 1) * a[i] % MOD
    res %= MOD
  print(res)

if __name__ == '__main__':
  main()
