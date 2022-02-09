import typing



def main() -> typing.NoReturn:
  n, k = map(int, input().split())


  cnt = 1 + 3 * (n - 1) + 3 * 2 * (k - 1) * (n - k)
  print(cnt / n ** 3)


main()
