def main():
  n, a, x, y = map(
    int,
    input().split(),
  )
  s = a * x
  s += max(0, (n - a) * y)
  print(s)

main()
