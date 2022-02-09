import typing
import numpy as np
import sys



def main() -> typing.NoReturn:
  n, m = map(
    int, input().split(),
  )
  inf = 1 << 40
  a = np.array(
    input().split(),
    dtype=np.int64,
  )
  b = np.array(
    input().split(),
    dtype=np.int64,
  )
  b = np.pad(
    b,
    1,
    constant_values=(
      -inf, inf,
    ),
  )
  a.sort()
  b.sort()
  i = np.searchsorted(b, a)
  d = np.minimum(
    np.abs(b[i] - a),
    np.abs(b[i - 1] - a),
  ).min()
  print(d)


main()
