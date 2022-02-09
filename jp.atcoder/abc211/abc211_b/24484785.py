import sys

def main():
  s = sys.stdin.read().split()
  s = set(s)
  t = {
    'H',
    '2B',
    '3B',
    'HR',
  }
  print(
    'Yes' if not (t - s)
    else 'No',
  )

main()
