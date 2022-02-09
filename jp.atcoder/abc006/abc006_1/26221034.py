import typing


def main() -> typing.NoReturn:
  n = input()
  ans = 'YES' if '3' in n or int(n) % 3 == 0 else 'NO'
  print(ans)


main()
