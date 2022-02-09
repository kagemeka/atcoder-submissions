import sys


def main():
  a, b, c = map(
    int,
    input().split(),
  )
  x = 2 * b - a - c
  k = max(0, (1 - x) // 2)
  print(x + 3 * k)


main()
