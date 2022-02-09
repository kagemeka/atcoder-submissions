																																	import typing
import numpy as np
import numba as nb


@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> typing.NoReturn:

  pow_10 = np.empty(10, np.int64)
  pow_10[0] = 1
  for i in range(9):
    pow_10[i + 1] = pow_10[i] * 10

  print(pow_10)
  cnt = 0
  for i in range(9):
    q, r = divmod(n, pow_10[i + 1])
    cnt += q * pow_10[i]
    cnt += max(0, min(2 * pow_10[i] - 1, r) - pow_10[i] + 1)
  print(cnt)


def main() -> typing.NoReturn:
  # consider per digit
  n = int(input())
  solve(n)


main()
