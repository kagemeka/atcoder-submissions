import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def fw_set(fw: np.ndarray, i: int, x: int) -> typing.NoReturn:
  while i < len(fw):
    fw[i] += x
    i += i & -i

@nb.njit
def fw_get(fw: np.ndarray, i: int) -> int:
  v = 0
  while i > 0:
    v += fw[i]
    i -= i & -i
  return v


@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(
  c: np.ndarray,
  lr: np.ndarray,
) -> typing.NoReturn:
  n, q = len(c), len(lr)

  buf = np.full(n + 1, -1, np.int64)
  prev = np.empty(n, np.int64)
  for i in range(n):
    prev[i] = buf[c[i]]
    buf[c[i]] = i + 1
  st = np.vstack((prev, np.arange(n) + 1)).T
  st = st[np.argsort(st[:, 0])]
  sort_idx = np.argsort(lr[:, 0])
  lr = lr[sort_idx]
  original_idx = np.arange(q)[sort_idx]

  res = np.empty(q, np.int64)
  fw = np.zeros(n + 1, np.int64)
  j = n - 1
  for i in range(q - 1, -1, -1):
    l, r = lr[i]
    while st[j, 0] >= l:
      fw_set(fw, st[j, 1], 1)
      j -= 1
    res[original_idx[i]] = (r - l + 1) - fw_get(fw, r)
  for x in res:
    print(x)



def main() -> typing.NoReturn:
  n, q = map(int, input().split())
  c = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  lr = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(q, 2)
  solve(c, lr)


main()
