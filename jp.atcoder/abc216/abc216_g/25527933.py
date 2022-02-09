import typing
import sys
import numpy as np
import numba as nb


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  lrx: np.ndarray,
) -> typing.NoReturn:
  fw_e = 0
  fw_fn = lambda x, y: x + y
  fw = np.full(n + 1, fw_e, np.int64)

  def fw_get(i):
    nonlocal fw, fw_fn, fw_e
    v = fw_e
    while i > 0:
      v = fw_fn(v, fw[i])
      i -= i & -i
    return v

  def fw_set(i, x):
    nonlocal fw, fw_fn
    while i < len(fw):
      fw[i] = fw_fn(fw[i], x)
      i += i & -i

  sort_idx = np.argsort(lrx[:, 1], kind='mergesort')
  lrx = lrx[sort_idx]
  a = np.zeros(n, np.int64)
  i = 0
  st = []
  for k in range(len(lrx)):
    l, r, x = lrx[k]
    while i < r:
      st.append(i)
      i += 1
    c = fw_get(r) - fw_get(l - 1)
    for _ in range(x - c):
      j = st.pop()
      fw_set(j + 1, 1)
      a[j] = 1
  return a


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lrx = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  a = solve(n, lrx)
  print(*a)


main()
