import typing


def main() -> typing.NoReturn:
  n = int(input())
  s = input()

  cnt = 1
  for i in range(n - 1):
    cnt += s[i] != s[i + 1]
  print(cnt)


main()
