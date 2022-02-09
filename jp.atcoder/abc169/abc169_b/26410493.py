import typing



def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(int, input().split())
  a.sort()
  mx = 10 ** 18
  p = 1
  for x in a:
    if x > mx // p:
      print(-1)
      return
    p *= x
    if p == 0:
      print(0)
      return
  print(p)


main()
