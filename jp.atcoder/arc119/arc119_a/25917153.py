import typing


def main() -> typing.NoReturn:
  n = int(input())


  ans = 1 << 60
  b = 0
  while 1 << b <= n:
    a, c = divmod(n, 1 << b)
    ans = min(ans, a + b + c)
    b += 1
  print(ans)


main()
