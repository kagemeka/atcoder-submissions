import typing
import sys
import numpy as np
import numba as nb


# @nb.njit
# def choose_pascal(n: int) -> np.ndarray:
#   c = np.zeros((n, n), np.float64)
#   c[:, 0] = 1
#   for i in range(1, n):
#     for j in range(1, i + 1):
#       c[i, j] = c[i - 1, j] + c[i - 1, j - 1] / 4
#   return c

def choose_pascal(n: int) -> typing.List[typing.List[int]]:
  c = [[0] * n for _ in range(n)]
  for i in range(n): c[i][0] = 1
  for i in range(1, n):
    for j in range(1, i + 1):
      c[i][j] = c[i - 1][j] + c[i - 1][j - 1] / 4
  return c


# @nb.njit((nb.i8, nb.i8, nb.i8, nb.i8), cache=True)
def solve(n: int, d: int, x: int, y: int) -> typing.NoReturn:
  if x % d or y % d:
    print(0)
    return
  x //= d
  y //= d
  if n < x + y or (n - x - y) & 1:
    print(0)
    return

  p = choose_pascal(1 << 10)

  k = n - x - y
  tot = 0
  for i in range(0, k + 1, 2):
    d = i // 2
    u = y + d
    l = (k - i) // 2
    r = x + l
    # tmp = p[n, d] * p[n - d, u]
    # tmp *= p[n - d - u, l] * p[n - d - u - l, r]

    tmp = p[n][d] * p[n - d][u]
    tmp *= p[n - d - u][l] * p[n - d - u - l][r]
    tot += tmp

  print(tot)


def main() -> typing.NoReturn:
  n, d = map(int, input().split())
  x, y = map(int, input().split())
  solve(n, d, x, y)

main()
