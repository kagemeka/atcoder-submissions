import typing


def main() -> typing.NoReturn:
  n = int(input())
  res = []
  while n:
    if n & 1:
      res.append(0)
      n -= 1
      continue
    res.append(1)
    n >>= 1
  res = map(lambda x: chr(ord('A') + x), res)
  res = ''.join(res)[::-1]
  print(res)



main()
