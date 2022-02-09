import typing




def main() -> typing.NoReturn:
  s = input()
  k = int(input())

  print(len(set(s[i:i + k] for i in range(len(s)- k + 1))))


main()
