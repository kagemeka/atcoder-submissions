import typing


def main() -> typing.NoReturn:
  s = input()
  t = input()
  w = ''
  n = len(t)
  for i in range(n):
    w += s[i] + t[i]
  if len(s) > n:
    w += s[-1]
  print(w)


main()
