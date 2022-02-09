import typing
import sys
import numpy as np




def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  print(a.sum() - a.min() * h * w)


main()
