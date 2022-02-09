import typing
import sys



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  *r, = map(int, input().split())
  r.sort()

  v = 0
  for x in r[-k:]:
    v = (v + x) / 2
  print(v)


main()
