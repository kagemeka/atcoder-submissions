import typing



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *a, = map(int, input().split())

  k = 1 << 20
  s = [True] * k
  for x in a: s[x] = False

  a = [True] * (m + 1)
  a[0] = False
  for i in range(2, m + 1):
    if all(s[j] for j in range(i, k, i)): continue
    for j in range(i, m + 1, i): a[j] = False

  print(sum(a))
  for i in range(m + 1):
    if a[i]: print(i)


main()
