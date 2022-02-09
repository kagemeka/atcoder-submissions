import sys

import numpy as np
MOD = 10 ** 9 + 7
U = 10 ** 6
def mod_cumprod(a, p=MOD):
  l = len(a); sql = int(np.sqrt(l) + 1)
  a = np.resize(a, sql**2).reshape(sql, sql)
  for i in range(sql - 1): a[:, i+1] *= a[:, i]; a[:, i+1] %= p
  for i in range(sql - 1): a[i+1] *= a[i, -1]; a[i+1] %= p
  return np.ravel(a)[:l]

def make_fac_ifac(n=U, p=MOD):
  fac = np.arange(n + 1); fac[0] = 1
  fac = mod_cumprod(fac)
  ifac = np.arange(n + 1, 0, -1); ifac[0] = pow(int(fac[-1]), p-2, p)
  ifac = mod_cumprod(ifac)[n::-1]
  return fac, ifac

fac, ifac = make_fac_ifac()

def mod_choose(n, r, p=MOD):
  if r > n or r < 0: return 0
  return fac[n] * ifac[r] % p * ifac[n-r] % p

def make_choose_n_table(n=10 ** 9, r=U, p=MOD):
  table = [None] * (r + 1)
  table = np.arange(n + 1, n - r, -1); table[0] = 1
  table[1:] = mod_cumprod(table[1:]) * ifac[1:r+1] % p
  return table

mod_choose_n = make_choose_n_table()

n, m = map(int, sys.stdin.readline().split())

def main():
  d = abs(n - m)
  if d >= 2: res = 0
  elif d == 1: res = fac[n] * fac[m] % MOD
  else: res = fac[n] * fac[m] % MOD * 2 % MOD
  print(res)

if __name__ == '__main__':
  main()
