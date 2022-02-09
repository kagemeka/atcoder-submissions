import typing



def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  s = [input() for _ in range(h)]

  t = []
  for row in s:
    t.append(row)
    t.append(row)


  print('\n'.join(t))


main()
