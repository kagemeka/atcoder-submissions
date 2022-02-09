import typing



def main() -> typing.NoReturn:
  s = input()
  t = input()
  n = len(s)

  atcoder = set('atcoder')

  for i in range(n):
    if s[i] == t[i]: continue
    if s[i] == '@' and t[i] in atcoder: continue
    if t[i] == '@' and s[i] in atcoder: continue
    print('You will lose')
    return


  print('You can win')


main()
