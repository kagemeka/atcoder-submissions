import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
  dx = c - a
  dy = d - b
  res = 'U' * dy + 'R' * (dx + 1) + 'D' * (dy + 1) + 'L' * (dx + 1)
  res += 'UL'
  res += 'U' * (dy + 1) + 'R' * (dx + 1) + 'D' * (dy + 1) + 'L' * dx
  print(res)

if __name__ == '__main__':
  main()
