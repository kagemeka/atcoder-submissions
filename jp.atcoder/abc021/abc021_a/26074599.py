import typing


def main() -> typing.NoReturn:
  n = int(input())

  a = []
  for i in range(10):
    if n >> i & 1:
      a.append(1 << i)

  print(len(a))
  print(*a, sep='\n')


main()
