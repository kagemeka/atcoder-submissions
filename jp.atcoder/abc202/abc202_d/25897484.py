import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def dfs(a: int, b: int, cache: np.ndarray) -> int:
  if cache[a, b]: return cache[a, b]
  cnt = 0
  for i in range(a + 1):
    cnt += dfs(i, b - 1, cache)
  cache[a, b] = cnt
  return cnt


@nb.njit((nb.i8, nb.i8, nb.i8), cache=True)
def solve(a: int, b: int, k: int) -> typing.NoReturn:

  cache = np.zeros((a + 1, b + 1), np.int64)
  cache[0] = 1
  cache[:, 0] = 1
  for i in range(a + 1):
    for j in range(b + 1):
      dfs(i, j, cache)


  res = np.empty(a + b, np.int64)
  i = 0
  while k:
    if cache[a, b] == k:
      res[i:i + b] = 1
      res[i + b:i + a + b] = 0
      k -= cache[a, b]
      break
    d = cache[a, b] - cache[a, b - 1]
    if k > d:
      k -= d
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
