import typing



def main() -> typing.NoReturn:
  s = input()
  s = s + '$'
  n = len(s)

  cnt = 1
  t = ''
  for i in range(n - 1):
    if s[i + 1] == s[i]:
      cnt += 1
      continue
    t += s[i] + str(cnt)
    cnt = 1
  print(t)


main()
