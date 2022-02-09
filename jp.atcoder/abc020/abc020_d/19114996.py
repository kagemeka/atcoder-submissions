def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


import numba as nb

@nb.njit((nb.i8, ), cache=True)
def find_divisors(n: int=...):
  m = int(n**.5) + 1
  divisors = []
  for x in range(1, m):
    if n%x: continue
    divisors.append(x)
    if n//x != x:
      divisors.append(n//x)
  divisors.sort()
  return divisors


@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n, k):
  mod = 10**9 + 7
  divs = find_divisors(k)[::-1]
  l = len(divs)
  s = [0] * l
  for i in range(l):
    d = divs[i]
    q = n // d
    tmp = d*(1 + q)*q//2 % mod
    for j in range(i):
      if divs[j] % d != 0: continue
      tmp -= s[j]
      tmp %= mod
    s[i] = tmp

  res = 0
  for i in range(l):
    res += k // divs[i] * s[i] % mod
    res %= mod
  print(res)


def main():
  n, k = readline_ints()
  solve(n, k)


if __name__ == '__main__':
  main()
