import typing



def main() -> typing.NoReturn:
  n = int(input())
  solve(n)


def solve(n: int) -> typing.NoReturn:
  cnt = n
  for i in range(1, n + 1):
    cnt -= '7' in str(i) or '7' in oct(i)
  print(cnt)


main()
