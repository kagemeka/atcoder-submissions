import typing
import numpy as np
import sys



def main() -> typing.NoReturn:
  n, m = map(
    int, input().split(),
  )
  a = np.array(
    input().split(),
    dtype=np.int64,
  )
  b = np.array(
    input().split(),
    dtype=np.int64,
  )
  a.sort()
  b.sort()

  i = np.searchsorted(
    b,
    a,
    side='left',
  )
  j = np.maximum(i - 1, 0)
  i = np.minimum(i, m - 1)
  k = np.searchsorted(
    b,
    a,
    side='right',
  )
  l = np.maximum(k - 1, 0)
  k = np.minimum(k, m - 1)


  cand = np.hstack((
    np.abs(a - b[i]),
    np.abs(a - b[j]),
    np.abs(a - b[k]),
    np.abs(a - b[l]),
  ))
  print(cand.min())





main()
