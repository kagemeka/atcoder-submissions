import typing
import sys
import itertools


def solve(
  k: int,
  vw: typing.List[typing.Tuple[str, str]],
) -> typing.NoReturn:


  def is_ok(l: typing.Tuple[int]) -> bool:
    s = [None] * k
    for v, w in vw:
      i = 0
      for d in v:
        d = int(d) - 1
        if i + l[d] > len(w): return False
        if s[d] and w[i:i + l[d]] != s[d]: return False
        s[d] = w[i:i + l[d]]
        i += l[d]
        continue
      if i < len(w): return False
    print(*s, sep='\n')
    return True

  for l in itertools.product((1, 2, 3), repeat=k):
    if is_ok(l): return



def main() -> typing.NoReturn:
  k, n = map(int, input().split())
  vw = list(zip(*[iter(sys.stdin.read().split())] * 2))
  solve(k, vw)


main()
