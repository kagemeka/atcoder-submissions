import typing
import numpy as np
import numba as nb


@nb.njit((nb.i8, ), cache=True)
def solve(k: int) -> typing.NoReturn:
  rem_appered = np.zeros(k, np.bool8)
  r = 0
  for i in range(k):
    r = (r * 10 + 7) % k
    if r == 0:
      print(i + 1)
      return
    if rem_appered[r]:
      print(-1)
      return
    rem_appered[r] = True



def main() -> typing.NoReturn:
  k = int(input())
  solve(k)


main()
