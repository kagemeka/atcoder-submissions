import typing
import numpy as np
import sys



def solve(
  n: int,
  k: int,
  c: int,
  a: int,
) -> typing.NoReturn:
  mod = 998244353

  if np.unique(a).size != k:
    print(0)
    return

  i = c == 0
  l = a[i]
  r = a[~i]
  a = np.zeros(
    n + 1,
    dtype=np.int64,
  )
  a[0] -= l.size
  a[l] += 1
  a[r + 1] -= 1
  a[-1] += r.size
  a = a.cumsum()[:-1]
  a += k
  a[l] = 1
  a[r] = 1
  b = list(a)
  p = 1

  for x in b:
    p *= x
    p %= mod
  print(p)



def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  c, a = np.array(
    sys.stdin.read().split(),
  ).reshape(k, 2).T
  a = a.astype(np.int64) - 1
  c = np.where(c == 'L', 0, 1)
  solve(n, k, c, a)


main()
