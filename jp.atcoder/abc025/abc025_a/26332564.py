import typing



def main() -> typing.NoReturn:
  s = input()
  n = int(input())

  q, r = divmod(n - 1, len(s))
  print(s[q] + s[r])


main()
