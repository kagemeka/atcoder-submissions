import typing
import sys
import numpy as np


def gcd(a: int, b: int) -> int:
  return gcd(b, a % b) if b else a


def solve(l: int) -> typing.NoReturn:
  a, b = 1, 1
  for i in range(11):
    a *= l - 1 - i
    b *= i + 1
    g = gcd(a, b)
    a //= g
    b //= g
  print(a // b)


def main() -> typing.NoReturn:
  l = int(input())
  solve(l)


main()
