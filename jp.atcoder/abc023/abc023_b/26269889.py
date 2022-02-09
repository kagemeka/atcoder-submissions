import typing


def make(n: int) -> str:
  if n == 0: return 'b'
  s = make(n - 1)
  if n % 3 == 1: return 'a' + s + 'c'
  if n % 3 == 2: return 'c' + s + 'a'
  return 'b' + s + 'b'


def main() -> typing.NoReturn:
  n = int(input())
  s = input()

  m = len(s)
  if m % 2 == 0:
    print(-1)
    return

  m >>= 1
  t = make(m)
  print(m if t == s else -1)



main()
