import typing
import numpy as np


def find_divisors(
  n: int,
) -> np.array:
  i = np.arange(int(n ** .5))
  i += 1
  i = i[n % i == 0]
  i = np.hstack((i, n // i))
  return np.unique(i)



def solve(
  p: int,
) -> typing.NoReturn:
  mod = 998244353
  n = p - 1
  divs = find_divisors(n)[::-1]
  l = len(divs)
  cnt = np.zeros(l, np.int64)
  for i in range(l):
    d = divs[i]
    c = n // d
    for j in range(i):
      if divs[j] % d: continue
      c -= cnt[j]
    c %= mod
    cnt[i] = c

  s = 1
  for i in range(l):
    d, c = divs[i], cnt[i]
    s += n // d % mod * c
    s %= mod
  print(s)



def main() -> typing.NoReturn:
  p = int(input())
  solve(p)



import sys
OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import i8, njit
  find_divisors = njit(
    find_divisors,
  )
  fn = solve
  signature = (i8, )

  from numba.pycc import CC
  cc = CC('my_module')
  cc.export(
    fn.__name__,
    signature,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
