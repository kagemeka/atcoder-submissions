import typing
import sys
import bisect


def main() -> typing.NoReturn:
  x = int(input())

  def check_ok(t: int) -> bool:
    return t * (t + 1) >= 2 * x


  def binary_search() -> int:
    lo, hi = 0, 1 << 30
    while hi - lo > 1:
      t = (lo + hi) // 2
      if check_ok(t):
        hi = t
      else:
        lo = t
    return hi


  print(binary_search())


main()
