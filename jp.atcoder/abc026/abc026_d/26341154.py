import typing
import sys
import numpy as np
import scipy.optimize



# @nb.njit((nb.i8, ) * 3, cache=True)
def solve(a: int, b: int, c: int) -> typing.NoReturn:

  def f(t: float) -> float:
    return a * t + b * np.sin(c * t * np.pi)


  def g(t: float) -> bool:
    return f(t) - 100

  t = scipy.optimize.newton(g, 0)
  print(t)



def main() -> typing.NoReturn:
  a, b, c = map(int, input().split())
  solve(a, b, c)


main()
