import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def repeated_combinations(n: int, k: int) -> np.ndarray:
  assert k >= 1
  res = np.empty((1 << 20, k), np.int64)
  idx_to_add = 0
  def add_result(a):
    nonlocal idx_to_add
    res[idx_to_add] = a
    idx_to_add += 1

  que = [(np.zeros(k, np.int64), 0)]
  for a, i in que:
    if i == k:
      add_result(a)
      continue
    for j in range(a[i - 1], n):
      b = a.copy()
      b[i] = j
      que.append((b, i + 1))
  return res[:idx_to_add]


@nb.njit
def enumerate_fx() -> np.ndarray:
  a = repeated_combinations(10, 11)
  m = len(a)
  fx = np.empty(m, np.int64)
  for i in range(m):
    fx[i] = np.prod(a[i])
  return np.unique(fx)


@nb.njit
def f(x: int) -> int:
  p = 1
  while x:
    x, r = divmod(x, 10)
    p *= r
  return p


@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n: int, b: int) -> typing.NoReturn:
  cands = enumerate_fx() + b
  cnt = 0
  for x in cands:
    cnt += 1 <= x <= n and x - f(x) == b
  print(cnt)


def main() -> typing.NoReturn:
  n, b = map(int, input().split())
  solve(n, b)


main()
