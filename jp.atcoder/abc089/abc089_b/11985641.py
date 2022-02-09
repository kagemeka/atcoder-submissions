import sys
n, *s = sys.stdin.read().split()

def main():
  print('Four' if len(set(s)) == 4 else 'Three')

if __name__ == '__main__':
  main()
