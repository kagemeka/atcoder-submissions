from copyreg import add_extension
import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8), cache=True)
def repeated_permutations(n: int, k: int) -> np.ndarray:
  res = np.empty((n ** k, k), np.int64)
  idx_to_add = 0
  def add_result(a):
    nonlocal idx_to_add
    res[idx_to_add] = a
    idx_to_add += 1

  que = [(np.empty(k, np.int64), 0)]
  for a, i in que:
    if i == k:
      add_result(a)
      continue
    for j in range(n):
      b = a.copy()
      b[i] = j
      que.append((b, i + 1))
  return res


@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> np.ndarray:
  res = np.empty(1 << n, np.int64)
  idx_to_add = 0
  def add_result(s):
    nonlocal idx_to_add
    res[idx_to_add] = s
    idx_to_add += 1

  for s in range(1 << n):
    l = 0
    ok = True
    for j in range(n):
      l += (~s >> j & 1) * 2 - 1
      if l >= 0: continue
      ok = False
      break
    ok &= l == 0
    if ok: add_result(s)

  res = res[:idx_to_add]
  return res

def main() -> typing.NoReturn:
  n = int(input())
  res = solve(n)
  res = list(res)
  for i, s in enumerate(res):
    a = ['(' if ~s >> j & 1 else ')' for j in range(n)]
    res[i] = ''.join(a)
  res.sort()
  print(*res, sep='\n')



main()
