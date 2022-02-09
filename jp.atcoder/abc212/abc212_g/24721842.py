import typing
import numpy as np
import numba as nb

@nb.njit
def find_divisors(
  n: int,
) -> np.array:
  i = np.arange(int(n ** .5))
  i += 1
  i = i[n % i == 0]
  i = np.hstack((i, n // i))
  return np.unique(i)



@nb.njit(
  (nb.i8, ),
  cache=True,
)
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


main()
