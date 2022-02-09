import typing


def main() -> typing.NoReturn:
  n = int(input())
  n = 2025 - n
  for i in range(1, 10):
    if n % i or n // i >= 10: continue
    print(f'{i} x {n // i}')


main()
