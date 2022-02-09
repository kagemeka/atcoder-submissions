import typing



def main() -> typing.NoReturn:
  *l, = map(int, input().split())
  l.sort()
  if l[0] == l[1]:
    print(l[2])
  else:
    print(l[0])


main()
