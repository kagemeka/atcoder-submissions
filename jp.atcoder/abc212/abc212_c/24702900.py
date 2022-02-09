import typing



def main() -> typing.NoReturn:
  n, m = map(
    int, input().split(),
  )
  a = sorted(map(
    int, input().split(),
  ))
  b = sorted(map(
    int, input().split(),
  ))
  i = j = 0
  mn = 1 << 40
  while i < n and j < m:
    mn = min(
      mn,
      abs(a[i] - b[j]),
    )
    if a[i] > b[j]:
      j += 1
    else:
      i += 1
  print(mn)


main()
