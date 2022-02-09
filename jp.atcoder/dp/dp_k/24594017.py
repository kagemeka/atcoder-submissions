import typing
import sys
import numpy as np



def solve(
  k: int,
  a: np.array,
) -> typing.NoReturn:
  win = np.zeros(
    1 << 18,
    dtype=np.bool8,
  )
  for i in range(k):
    win[i + a] |= ~win[i]

  print(
    'First' if win[k]
    else 'Second',
  )


def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(k, a)



OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import i8
  from numba.pycc import CC
  cc = CC('my_module')

  fn = solve
  signature = (i8, i8[:])

  cc.export(
    fn.__name__,
    signature,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
