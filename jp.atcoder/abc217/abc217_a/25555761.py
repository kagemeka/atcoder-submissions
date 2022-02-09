import typing



def main() -> typing.NoReturn:
  s, t = input().split()
  if s < t:
    print('Yes')
  else:
    print('No')



main()
