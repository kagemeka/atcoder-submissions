import sys



def main():
  a, b, c = map(
    int,
    input().split(),
  )
  d = 2 * b - a - c
  if d >= 0:
    print(d)
    return
  q, r = divmod(d, 2)
  print(-q + r)


main()
