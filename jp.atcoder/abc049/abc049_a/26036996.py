import typing


def main() -> typing.NoReturn:
  vowels = set('aeiou')
  c = input()
  ans = 'vowel' if c in vowels else 'consonant'
  print(ans)

main()
