import typing
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(s: np.ndarray) -> typing.NoReturn:
  n = len(s)
  pos = (s == 1).cumsum()
  neg = (s == -1).cumsum()
  a = pos - neg
  b = a[s == 0]
  m = len(b)
  sort_idx = np.argsort(b)
  d = np.full(m, -1, np.int64)
  d[sort_idx[:m // 2]] += 2

  j = 0
  x = 0
  h = 0
  for i in range(n):
    if s[i] == 0:
      x += d[j]
      j += 1
      continue
    h += x * s[i]

  print(h)




def main() -> typing.NoReturn:
  s = input().replace('M','1').replace('-', '0')
  s = s.replace('+', '2')
  *s, = map(int, s)
  s = np.array(s) - 1
  solve(s)


main()
