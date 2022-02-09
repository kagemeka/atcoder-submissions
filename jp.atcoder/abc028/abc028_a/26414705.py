import typing


def main() -> typing.NoReturn:
  n = int(input())

  if n < 60:
    ans = 'Bad'
  elif n < 90:
    ans = 'Good'
  elif n < 100:
    ans = 'Great'
  else:
    ans = 'Perfect'
  print(ans)


main()
