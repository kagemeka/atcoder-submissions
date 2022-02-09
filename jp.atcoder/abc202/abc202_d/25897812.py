import typing
import sys
import numpy as np
import numba as nb




@nb.njit
def choose_pascal(n: int) -> np.ndarray:
  choose = np.zeros((n + 1, n + 1), np.int64)
  choose[:, 0] = 1
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      choose[i, j] = choose[i - 1, j] + choose[i - 1, j - 1]
  return choose


@nb.njit((nb.i8, nb.i8, nb.i8), cache=True)
def solve(a: int, b: int, k: int) -> typing.NoReturn:
  choose = choose_pascal(60)

  res = np.empty(a + b, np.int64)
  i = 0
  while k:
    if choose[a + b, a] == k:
      res[i:i + b] = 1
      res[i + b:] = 0
      break
    if k > choose[a + b - 1, b]:
      k -= choose[a + b - 1, b]
      b -= 1
      res[i] = 1
    else:
      a -= 1
      res[i] = 0
    i += 1
  return res


def main() -> typing.NoReturn:
  a, b, k = map(int, input().split())
  res = solve(a, b, k)
  print(''.join(map(chr, res + ord('a'))))


main()
