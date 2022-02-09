import typing


def main() -> typing.NoReturn:
  x = int(input())
  ans = 'Yes' if x >= 30 else 'No'
  print(ans)

main()
