import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def find_divisors(n: int) -> np.ndarray:
  i = np.arange(int(n ** .5)) + 1
  i = i[n % i == 0]
  return np.unique(np.hstack((i, n // i)))




@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n: int, k: int) -> typing.NoReturn:
  divs = find_divisors(k)
  mod = 10 ** 9 + 7

  m = len(divs)
  s = np.zeros(m, np.int64)
  for i in range(m):
    d = divs[i]
    s[i] = (d + n // d * d) * (n // d) // 2 % mod

  for i in range(m - 1, -1, -1):
    for j in range(i + 1, m):
      if divs[j] % divs[i]: continue
      s[i] -= s[j]
    s[i] %= mod

  cnt = 0
  for i in range(m):
    cnt += k // divs[i] * s[i] % mod
  print(cnt % mod)



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  solve(n, k)


main()
