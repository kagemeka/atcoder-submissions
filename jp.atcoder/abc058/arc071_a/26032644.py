import typing
import sys
import collections
import string


def main() -> typing.NoReturn:
  n = int(input())
  s = sys.stdin.read().split()


  cnt = collections.defaultdict(int)
  for x in string.ascii_lowercase:
    cnt[x] = 100

  for w in s:
    c = collections.Counter(w)
    for x in string.ascii_lowercase:
      cnt[x] = min(cnt[x], c[x])

  w = ''
  for x in string.ascii_lowercase:
    w += cnt[x] * x
  print(w)


main()
