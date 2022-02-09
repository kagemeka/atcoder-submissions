import typing



def main() -> typing.NoReturn:
  s = input()

  while s:
    if s[-5:] == 'dream' or s[-5:] == 'erase':
      s = s[:-5]
    elif s[-7:] == 'dreamer':
      s = s[:-7]
    elif s[-6:] == 'eraser':
      s = s[:-6]
    else:
      print('NO')
      return
  print('YES')


main()
