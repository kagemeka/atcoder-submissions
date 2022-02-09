import typing


def main() -> typing.NoReturn:
  s = input()
  n = len(s)

  ans = 'First' if n & 1 and s[0] != s[-1] else 'Second'
  print(ans)


main()
