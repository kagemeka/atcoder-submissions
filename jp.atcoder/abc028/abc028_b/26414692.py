import typing


def main() -> typing.NoReturn:
  s = input()
  a = [ord(x) - ord('A') for x in s]
  c = [0] * 6
  for x in a:
    c[x] += 1
  print(*c)


main()
