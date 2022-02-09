import typing



def main() -> typing.NoReturn:
  a, b, c = map(int, input().split())
  bl1 = a + b == c
  bl2 = a - b == c
  if bl1 and bl2:
    ans = '?'
  elif bl1:
    ans = '+'
  elif bl2:
    ans = '-'
  else:
    ans = '!'
  print(ans)


main()
