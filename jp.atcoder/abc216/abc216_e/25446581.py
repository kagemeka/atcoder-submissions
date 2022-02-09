import typing


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  *a, = map(int, input().split())
  k = min(k, sum(a))
  a.sort(reverse=1)
  a.append(0)

  c = 0
  h = 1 << 40
  for i in range(n + 1):
    if i > 0:
      x = (h * i - k + c + i - 1) // i
    else:
      x = -1
    if x > a[i]:
      c += i * (h - x)
      break
    x = a[i]
    c += i * (h - x)
    h = x

  h = x

  s = (k - c) * h
  for x in a:
    if x < h: break
    s += (h + 1 + x) * (x - h) // 2
  print(s)


main()
