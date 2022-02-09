import typing
import collections



def main() -> typing.NoReturn:
  mod = 10 ** 9 + 7
  n = int(input())
  s = input()
  t = '$atcoder'
  idx = {x: i for i, x in enumerate(t)}
  cnt = collections.defaultdict(int)
  cnt['$'] += 1
  for x in s:
    if not x in idx: continue
    cnt[x] += cnt[t[idx[x] - 1]]
    cnt[x] %= mod
  print(cnt['r'])


main()
