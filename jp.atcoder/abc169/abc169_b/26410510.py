import typing



def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(int, input().split())
  if 0 in a:
    print(0)
    return
  mx = 10 ** 18
  p = 1
  for x in a:
    if x > mx // p:
      print(-1)
      return
    p *= x
  print(p)


main()
