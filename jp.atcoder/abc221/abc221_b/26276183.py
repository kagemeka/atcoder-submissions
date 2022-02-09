import typing


def main() -> typing.NoReturn:
  s = input()
  t = input()
  if s == t:
    print('Yes')
    return

  n = len(s)
  for i in range(n - 1):
    a = list(s)
    a[i], a[i + 1] = a[i + 1], a[i]
    if ''.join(a) == t:
      print('Yes')
      return
  print('No')


main()
