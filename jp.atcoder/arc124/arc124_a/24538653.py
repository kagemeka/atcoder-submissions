import typing


mod = 998244353

def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )

  if k > n:
    print(0)
    return

  cs = []
  xs = []
  for _ in range(k):
    c, x = input().split()
    cs.append(c)
    xs.append(int(x) - 1)

  if len(set(xs)) < k:
    print(0)
    return



  a = [0] * (n + 1)
  for c, x in zip(cs, xs):
    if c == 'L':
      a[0] -= 1
      a[x] += 1
    else:
      a[x + 1] -= 1
      a[n] += 1

  for i in range(n):
    a[i + 1] += a[i]

  for i in range(n):
    a[i] += k

  for x in xs:
    a[x] = 1

  p = 1
  for x in a[:n]:
    p *= x
    p %= mod
  print(p)


main()
