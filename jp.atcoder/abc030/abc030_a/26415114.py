import typing



def main() -> typing.NoReturn:
  a, b, c, d = map(int, input().split())
  lhs, rhs = b * c, d * a
  ans = (
    'TAKAHASHI' if lhs > rhs
    else 'AOKI' if lhs < rhs
    else 'DRAW'
  )
  print(ans)


main()
