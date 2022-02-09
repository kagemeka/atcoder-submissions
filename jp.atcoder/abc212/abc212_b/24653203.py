def main():
  s = input()
  if len(set(s)) == 1:
    print('Weak')
    return

  *s, = map(int, list(s))

  for i in range(3):
    if (
      s[i + 1] != (s[i] + 1) % 10
    ):
      print('Strong')
      return

  print('Weak')


main()
