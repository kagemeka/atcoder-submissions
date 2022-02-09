def main():
  n, a, x, y = map(
    int,
    input().split(),
  )
  c = min(n, a)
  s = c * x + (n - c) * y
  print(s)

main()
