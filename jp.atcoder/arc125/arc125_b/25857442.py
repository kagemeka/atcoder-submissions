import typing
import numba as nb



@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> typing.NoReturn:
  mod = 998_244_353
  q = 1
  cnt = 0
  while q * q <= n:
    cnt += (n // q - q) // 2 + 1
    cnt %= mod
    q += 1
  print(cnt)


def main() -> typing.NoReturn:
  n = int(input())
  solve(n)


main()
