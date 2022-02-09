import typing


def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  *h, = map(
    int, input().split(),
  )
  inf = 1 << 30
  c = [inf] * (n + 1)
  c[0] = c[1] = 0
  h = [h[0]] + h
  for i in range(2, n + 1):
    x = inf
    for j in range(i - k, i):
      if j < 0: continue
      x = min(
        x,
        c[j] + abs(h[i] - h[j])
      )
    c[i] = x
  print(c[n])

main()
