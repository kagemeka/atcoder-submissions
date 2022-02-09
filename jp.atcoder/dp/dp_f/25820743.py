import typing
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def lcs(
  a: np.ndarray,
  b: np.ndarray,
) -> np.ndarray:
  n, m = a.size, b.size
  l = np.zeros((n + 1, m + 1), np.int64)
  for i in range(n):
    for j in range(m):
      l[i + 1][j + 1] = max(
        l[i][j + 1],
        l[i + 1][j],
        l[i][j] + (a[i] == b[j]),
      )


  k = l[-1][-1]
  s = np.empty(k, np.int64)
  i, j = n - 1, m - 1
  while i >= 0 and j >= 0:
    x = l[i + 1][j + 1]
    if l[i + 1][j] == x: j -= 1
    elif l[i][j + 1] == x: i -= 1
    else:
      k -= 1
      s[k] = a[i]
      i -= 1
      j -= 1
  return s



@nb.njit(
  (nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  s: np.array,
  t: np.array,
) -> np.array:
  return lcs(s, t)


def main() -> typing.NoReturn:
  *s, = map(ord, input())
  *t, = map(ord, input())
  s = np.array(s)
  t = np.array(t)
  res = solve(s, t)
  print(''.join(map(chr, res)))


main()
