import typing



def solve(n: int) -> typing.NoReturn:
  x = 1
  flg = n.bit_length() & 1

  turn = 0
  while x <= n:
    x = 2 * x + 1 if flg ^ turn else 2 * x
    turn ^= 1
  ans = 'Takahashi' if turn == 0 else 'Aoki'
  print(ans)


def main() -> typing.NoReturn:
  n = int(input())
  solve(n)


main()
