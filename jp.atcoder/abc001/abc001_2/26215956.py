import typing



def main() -> typing.NoReturn:
  m = int(input())

  if m < 100:
    vv = 0
  elif 100 <= m <= 5_000:
    vv = m // 100
  elif 6_000 <= m <= 30_000:
    vv = m // 1_000 + 50
  elif 35_000 <= m <= 70_000:
    vv = (m // 1_000 - 30) // 5 + 80
  elif 70_000 <= m:
    vv = 89
  else:
    raise

  print(f'{vv:02}')


main()
