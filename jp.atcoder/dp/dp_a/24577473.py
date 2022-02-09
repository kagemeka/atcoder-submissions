import typing


def main() -> typing.NoReturn:
  n = int(input())
  *h, = map(
    int, input().split(),
  )
  h = [h[0]] + h
  inf = 1 << 30
  c = [inf] * (n + 1)
  c[0] = c[1] = 0
  for i in range(2, n + 1):
    c[i] = min(
      c[i - 2]
      + abs(h[i] - h[i - 2]),
      c[i - 1]
      + abs(h[i] - h[i - 1]),
    )
  print(c[n])


main()
