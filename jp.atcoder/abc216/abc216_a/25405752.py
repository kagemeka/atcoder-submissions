import typing


def main() -> typing.NoReturn:
  a = float(input())
  x = int(a)
  y = int((a - x) * 10)
  print(y)
  if 0 <= y <= 2:

    print(f'{x}-')
  elif 3 <= y <= 6:
    print(x)
  else:
    print(f'{x}+')


main()
