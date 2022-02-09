import typing


def main() -> typing.NoReturn:
  s = input()
  n = len(s)
  cnt = sum(s[i] != s[i + 1] for i in range(n - 1))
  print(cnt)


main()
