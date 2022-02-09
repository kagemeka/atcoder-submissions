import typing


def main() -> typing.NoReturn:
  a, b, c = map(int, input().split())
  ans = 'YES' if 2 * b - a - c == 0 else 'NO'
  print(ans)

main()
