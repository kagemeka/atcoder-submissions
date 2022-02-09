import typing

def main() -> typing.NoReturn:
  n, w = map(int, input().split())
  print(n // w)

main()
