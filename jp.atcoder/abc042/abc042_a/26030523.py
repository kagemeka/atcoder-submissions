import typing



def main() -> typing.NoReturn:
  *a, = map(int, input().split())
  a.sort()
  ans = 'YES' if a[0] == a[1] == 5 and a[2] == 7 else 'NO'
  print(ans)


main()
