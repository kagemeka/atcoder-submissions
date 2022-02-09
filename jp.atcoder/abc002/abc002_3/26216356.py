import typing




def main() -> typing.NoReturn:
  x0, y0, x1, y1, x2, y2 = map(int, input().split())
  x1 -= x0
  y1 -= y0
  x2 -= x0
  y2 -= y0

  prod = x1 * y2 - x2 * y1
  print(abs(prod) / 2)


main()
