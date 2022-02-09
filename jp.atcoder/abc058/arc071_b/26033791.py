import typing 
import sys 
import numpy as np 
import numba as nb 


@nb.njit((nb.i8[:], ) * 2, cache=True)
def solve(x: np.ndarray, y: np.ndarray) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  def calc_sum(x):
    n = len(x)
    i = np.arange(n - 1)
    s = np.sum((i + 1) * x[i + 1] % mod) % mod
    s -= np.sum((n - 1 - i) * x[i] % mod) % mod
    return s % mod
  
  s = calc_sum(x) * calc_sum(y) % mod
  print(s)
    

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  x = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  y = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(x, y)           


main()