import typing



def main() -> typing.NoReturn:
  *a, = map(int, input().split())
  a.sort()
  ans = 'Yes' if a[0] + a[1] == a[2] else 'No'
  print(ans)


main()
