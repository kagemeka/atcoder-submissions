import typing



def main() -> typing.NoReturn:
  n = int(input())
  a, b = map(int, input().split())
  k = int(input())
  *p, = map(int, input().split())
  if len({a, b} | set(p)) != k + 2:
    print('NO')
  else:
    print('YES')

main()
