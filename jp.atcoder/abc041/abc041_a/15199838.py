import sys


def A():
  s, i = sys.stdin.read().split()
  i = int(i)
  print(s[i-1])

def main():
  A()


if __name__ == "__main__":
  main()
