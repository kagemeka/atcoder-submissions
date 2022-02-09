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
  res = np.empty((1 << n, n), np.int64)
  idx_to_add = 0
  def add_result(s):
    nonlocal idx_to_add
    res[idx_to_add] = s
    idx_to_add += 1

  perms = repeated_permutations(2, n)
  for i in range(len(perms)):
    p = perms[i]
    l = 0
    ok = True
    for j in p:
      l -= j * 2 - 1
      if l <= 0: continue
      ok = False
      break
    ok &= l == 0
    if ok: add_result(p)

  res = res[:idx_to_add]
  return res

def main() -> typing.NoReturn:
  n = int(input())
  res = solve(n)
  res = list(res)
  for i, a in enumerate(res):
    a = list(a)
    a = ['(' if x == 1 else ')' for x in a]
    res[i] = ''.join(a)
  res.sort()
  print(*res, sep='\n')



main()
