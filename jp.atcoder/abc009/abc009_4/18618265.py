from typing import Union, Tuple
import numpy as np
# from numba import njit, i8
MOD = 10 ** 9 + 7



class Modular(int):
  def __init__(self, n: int, mod: int=MOD):
    self.value = n
    self.mod = mod

  def __str__(self) -> str: return f'{self.value}'

  def __add__(self, other):
    return self.__class__((self.value + other.value) % self.mod)
  def __sub__(self, x): return self.__class__((self.value - x.value) % self.mod)
  def __mul__(self, x): return self.__class__((self.value * x.value) % self.mod)
  def __pow__(self, x): return self.__class__(pow(self.value, x.value, self.mod))

  def __lt__(self, x): return self.value < x.value
  def __le__(self, x): return self.value <= x.value
  def __eq__(self, x): return self.value == x.value
  def __ne__(self, x): return self.value != x.value
  def __gt__(self, x): return self.value > x.value
  def __ge__(self, x): return self.value >= x.value

Mint = Modular

class SemiGroup:
  ...
class Monoid:
  ...
class Group:
  ...
class SemiRing:
  ...
class Ring:
  ...



def identity(n: Union[int, np.int64]):
  return np.identity(n, dtype=np.int64)


def dot(a: np.ndarray = ..., b: np.ndarray = ...):
  return np.dot(a, b)



def matrix_pow(cls, a, n, mod=10**9+7):
  m = len(a)
  b = identity(m)
  while n:
    if n&1: b = dot(b, a)
    n >>= 1; a = dot(a, a)
    a %= mod; b %= mod

  return b


def bitwise_dot(a: np.ndarray, b: np.ndarray) -> np.ndarray:
  return np.bitwise_xor.reduce(a[:,None,:] & b.T[None,...], axis=-1)


def bitwise_matrix_power(a: np.ndarray = ..., n: int = ...):
  if n==0:
    return np.eye(len(a), dtype=np.uint32) * ((1<<32) - 1)
  res = bitwise_matrix_power(a, n//2)
  res = bitwise_dot(res, res)
  return bitwise_dot(res, a) if n&1 else res



# def cumprod_mod(a: np.ndarray = ..., mod: int = MOD) -> np.ndarray:
#   l = len(a)
#   n = int(np.sqrt(l) + 1)
#   a = np.resize(a, (n, n))
#   for i in range(n-1):
#     a[:, i+1] *= a[:, i]
#     a[:, i+1] %= mod
#   for i in range(n-1):
#     a[i+1] *= a[i, -1]
#     a[i+1] %= mod
#   return np.ravel(a)[:l]



@njit
def pow(x: int, n: int, mod: int = MOD):
  assert n >= 0
  if n == 0: return 1
  res = pow(x, n//2, mod) ** 2 % mod
  if n&1:
    res *= x
    res %= mod
  return res


@njit
def cumprod_mod(a: np.ndarray = ..., mod: int = MOD) -> np.ndarray:
  n = len(a)
  for i in range(n-1):
    a[i+1] *= a[i]
    a[i+1] %= mod
  return a


@njit
def make_factorial_table(max_n: int = 10**6, p: int = MOD) -> np.ndarray:
  n = max_n
  fact: np.ndarray = np.arange(n+1)
  fact[0] = 1
  fact: np.ndarray = cumprod_mod(fact, mod=p)
  return fact


@njit
def make_inverse_factorial_table(
    max_n: int = 10**6, p: int = MOD,
    fact: Union[np.ndarray, None] = None) -> np.ndarray:
  n = max_n
  if fact is None:
    fact = make_factorial_table(max_n=n, p=p)
  assert len(fact) == n+1
  inv_fact = np.arange(1, n+2)
  inv_fact[-1] = pow(fact[-1], p-2, p)
  inv_fact = cumprod_mod(inv_fact[::-1], mod=p)[n::-1]
  return inv_fact


@njit
def make_fact_and_inv_fact(
    max_n: int = 10**6, p: int = MOD) -> Tuple[np.ndarray, np.ndarray]:
  fact = make_factorial_table(max_n=max_n, p=p)
  inv_fact = make_inverse_factorial_table(fact=fact)
  return fact, inv_fact






class Kitamasa:
  pass


import sys


def d():
  k, m = map(int, sys.stdin.readline().split())
  a = np.array([int(x) for x in sys.stdin.readline().split()])
  c = np.array([int(x) for x in sys.stdin.readline().split()])
  mask = (1<<32) - 1
  d = np.eye(k, k, -1, dtype=np.uint32) * mask; d[0] = c
  if m <= k: print(a[m-1]); return
  res = bitwise_dot(bitwise_matrix_power(d, m-k), a[::-1].reshape(-1, 1))[0][0]
  print(res)



if __name__ == '__main__':
  d()
  ...
