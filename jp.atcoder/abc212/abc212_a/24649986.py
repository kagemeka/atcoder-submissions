

def main():
  a, b = map(
    int, input().split(),
  )
  c = a * b
  print(
    'Alloy' if c > 0 else
    'Gold' if 0 < a else
    'Silver'
  )

main()
