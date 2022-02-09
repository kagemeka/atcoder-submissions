import sys
n, *a = map(int, sys.stdin.read().split())

def main():
  x = round(sum(a) / n)
  s = sum([(x - i) ** 2 for i in a])
  print(s)

if __name__ == '__main__':
  main()
