import typing
import numpy as np



class LCS():

  def __call__(
    self,
    a: np.array,
    b: np.array,
  ) -> int:
    n, m = a.size, b.size
    l = np.zeros(
      (n + 1, m + 1),
      dtype=np.int64,
    )
    for i in range(n):
      np.maximum(
        l[i, :-1]
        + (a[i] == b),
        l[i, 1:],
        out=l[i + 1, 1:],
      )
      np.maximum.accumulate(
        l[i + 1],
        out=l[i + 1],
      )
    res = []
    i, j = n - 1, m - 1
    while i >= 0 and j >= 0:
      x = l[i + 1, j + 1]
      if l[i + 1, j] == x:
        j -= 1
        continue
      if l[i, j + 1] == x:
        i -= 1
        continue
      res.append(a[i])
      i -= 1; j -= 1
    return np.array(res)[::-1]



def solve(
  s: np.array,
  t: np.array,
) -> typing.NoReturn:
  lcs = LCS()
  res = lcs(s, t)
  # res = lcs.retrieve()
  print(''.join(map(chr, res)))



def main() -> typing.NoReturn:
  *s, = map(ord, input())
  *t, = map(ord, input())
  s = np.array(s)
  t = np.array(t)
  solve(s, t)


main()
