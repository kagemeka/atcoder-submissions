import typing
import sys
import numba as nb


def main() -> typing.NoReturn:
  n, m = map(int, input().split())


  x = y = z = 0
  if m & 1:
    y += 1
    m -= 3
    n -= 1
  z = m // 2 - n
  x = n - z
  if x >= 0 and y >= 0 and z >= 0:
    print(x, y, z)
  else:
    print(-1, -1, -1)


main()
