import typing


def main() -> typing.NoReturn:
  s = input()
  x, y = s.split('.')
  y = int(y)
  if 0 <= y <= 2:
    print(x + '-')
  elif 3 <= y <= 6:
    print(x)
  else:
    print(x + '+')


main()
