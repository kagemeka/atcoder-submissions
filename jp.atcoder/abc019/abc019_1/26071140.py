import typing


def main() -> typing.NoReturn:
  *a, = map(int, input().split())
  a.sort()
  print(a[1])

main()
