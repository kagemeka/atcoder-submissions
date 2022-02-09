import typing


def main() -> typing.NoReturn:
  m, d = map(int, input().split())
  ans = 'YES' if m % d == 0 else 'NO'
  print(ans)


main()
