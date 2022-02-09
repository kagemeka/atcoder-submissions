import typing


def main() -> typing.NoReturn:
  vowels = set('aeiou')

  s = input()
  print(''.join(c for c in s if not c in vowels))


main()
