def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def solve(s: str):
  global vowels
  s = ''.join([c for c in s if not c in vowels])
  print(s)


def main():
  global vowels
  vowels = set('aeiou')
  w = readline().decode()
  solve(w)


if __name__ == '__main__':
  main()
