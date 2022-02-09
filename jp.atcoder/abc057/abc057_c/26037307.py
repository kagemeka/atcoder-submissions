import typing



def main() -> typing.NoReturn:
  n = int(input())

  def digits_count(n: int) -> int:
    c = 0
    while n:
      n //= 10
      c += 1
    return c


  mn = 1 << 30
  i = 0

  while i * i < n:
    i += 1
    if n % i: continue
    mn = min(mn, digits_count(n // i))
  print(mn)


main()
