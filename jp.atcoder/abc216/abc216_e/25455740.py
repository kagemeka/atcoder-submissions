import typing


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  *a, = map(int, input().split())
  k = min(k, sum(a))

  def count(x: int) -> int:
    c = 0
    for h in a:
      c += max(0, h - x + 1)
    return c

  def binary_search() -> int:
    lo, hi = 0, 10 << 40
    while hi - lo > 1:
      x = (lo + hi) // 2
      if count(x) <= k:
        hi = x
      else:
        lo = x
    return hi

  x = binary_search()
  c = count(x)
  s = (k - c) * (x - 1)
  for h in a:
    s += max(0, (x + h) * (h - x + 1) // 2)
  print(s)


main()
