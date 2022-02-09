import sys

MOD = 10 ** 9 + 7
U = 10 ** 6
def make_fac_ifac(n=U, p=MOD):
  fac = [None] * (n + 1)
  fac[0] = 1
  for i in range(n): fac[i+1] = fac[i] * (i + 1) % p
  ifac = [None] * (n + 1)
  ifac[n] = pow(fac[n], p - 2, p)
  for i in range(n, 0, -1): ifac[i-1] = ifac[i] * i % p
  return fac, ifac

fac, ifac = make_fac_ifac()

def mod_choose(n, r, p=MOD):
  if r > n or r < 0: return 0
  return fac[n] * ifac[r] % p * ifac[n-r] % p

def make_choose_n_table(n=10 ** 9, r=U, p=MOD):
  table = [None] * (r + 1)
  table[0] = 1
  j = 1
  for i in range(n, n - r, -1):
    table[j] = table[j-1] * i % p
    j += 1
  for i in range(1, r + 1): table[i] = table[i] * ifac[i] % p
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
