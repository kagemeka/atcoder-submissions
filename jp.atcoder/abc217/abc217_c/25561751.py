import typing



def main() -> typing.NoReturn:
  n = int(input())
  *p, = map(int, input().split())

  q = [-1] * n
  for i in range(n):
    q[p[i] - 1] = i + 1
  print(*q)



main()
