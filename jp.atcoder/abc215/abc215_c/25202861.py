import typing
import itertools


def main() -> typing.NoReturn:
  s, k = input().split()
  k = int(k)
  perms = itertools.permutations(s)
  perms = sorted(set(perms))
  print(''.join(perms[k - 1]))


main()
