import typing
import itertools



def solve(s: str) -> typing.NoReturn:
  n = 10
  cand = []
  must = 0
  for i in range(n):
    if s[i] == 'o':
      cand.append(i)
      must |= 1 << i
    if s[i] == '?':
      cand.append(i)

  cnt = 0
  for prod in itertools.product(cand, repeat=4):
    res = 0
    for i in prod:
      res |= 1 << i
    cnt += must & ~res == 0

  print(cnt)



def main() -> typing.NoReturn:
  s = input()
  solve(s)


main()
