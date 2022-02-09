import typing


def gcd(a: int, b: int) -> int:
  return gcd(b, a % b) if b else a


def lcm(a: int, b: int) -> int: return a // gcd(a, b) * b


def main() -> typing.NoReturn:
  a = int(input())
  b = int(input())
  n = int(input())
  l = lcm(a, b)
  print((n + l - 1) // l * l)


main()
