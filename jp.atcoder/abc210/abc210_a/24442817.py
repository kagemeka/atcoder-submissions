def main():
  n, a, x, y = map(
    int,
    input().split(),
  )
  s = a * x + (n - a) * y
  print(s)

main()
