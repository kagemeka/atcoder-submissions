import typing



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *s, = map(int, input().split())
  *t, = map(int, input().split())
  if set(t) - set(s):
    print(-1)
    return

  cnt = m
  t = [s[0]] + t
  for i in range(m):
    cnt += t[i] != t[i + 1]
  if cnt == m:
    print(cnt)
    return
  cnt -= 1
  cnt += min(s.index(s[0] ^ 1), s[::-1].index(s[0] ^ 1) + 1)
  print(cnt)


main()
