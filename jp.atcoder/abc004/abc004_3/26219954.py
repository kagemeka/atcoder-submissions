import typing




def main() -> typing.NoReturn:
  a = list(range(1, 7))
  n = len(a)
  k = int(input())
  k %= n * (n - 1)
  q, r = divmod(k, n - 1)
  a = a[q:] + a[:q]
  for i in range(r):
    a[i], a[i + 1] = a[i + 1], a[i]
  print(''.join(map(str, a)))


main()
