import typing 


def main() -> typing.NoReturn:
  a = float(input())
  x = int(a)
  y = round((a - x) * 10) 
  if 0 <= y <= 2:
    print(f'{x}-')
  elif 3 <= y <= 6:
    print(x)
  else:
    print(f'{x}+')


main()