import typing


def main() -> typing.NoReturn:
  n = int(input())
  s = input()

  if n & 1 ^ 1:
    print(-1)
    return

  a = tuple('abc')
  i = (1 - n // 2) % 3
  for c in s:
    if c != a[i]:
      print(-1)
      return
    i = (i + 1) % 3
  print(n // 2)


main()
