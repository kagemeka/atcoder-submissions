def main():
  n = int(input())
  s = input()
  for i in range(n):
    if s[i] == '0': continue
    break
  print(
    'Aoki' if i & 1
    else 'Takahashi',
  )


main()
