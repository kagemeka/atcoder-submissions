import typing


def main() -> typing.NoReturn:
  s = input().split()
  t = ''.join(w[0] for w in s)
  print(t)


main()
