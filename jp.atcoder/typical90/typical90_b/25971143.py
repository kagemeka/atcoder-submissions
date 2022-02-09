from copyreg import add_extension
import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8[:]), cache=True)
def next_repeated_permutation(
  n: int,
  a: np.ndarray,
) -> typing.NoReturn:
  for i in range(a.size - 1, -1, -1):
    a[i] += 1
    if a[i] < n: return
    a[i] = 0
  a[:] = -1


@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> np.ndarray:
  res = np.empty((1 << n, n), np.int64)
  idx_to_add = 0
  def add_result(s):
    nonlocal idx_to_add
    res[idx_to_add] = s
    idx_to_add += 1

  p = np.zeros(n, np.int64)
  while p[0] != -1:
    l = 0
    ok = True
    for j in p:
      l -= j * 2 - 1
      if l <= 0: continue
      ok = False
      break
    ok &= l == 0
    if ok: add_result(p)
    next_repeated_permutation(2, p)

  res = res[:idx_to_add]
  return res[::-1]

def main() -> typing.NoReturn:
  n = int(input())
  res = solve(n)
  res = list(res)
  for i, a in enumerate(res):
    a = list(a)
    a = ['(' if x == 1 else ')' for x in a]
    res[i] = ''.join(a)
  print(*res, sep='\n')



main()
