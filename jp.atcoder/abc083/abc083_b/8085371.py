n, a, b = map(int, input().split())
total = 0

def sum_digits(digits):
  return sum(int(digit) for digit in str(digits))

for i in range(1, n+1):
  total_digits = sum_digits(i)
  if total_digits >= a and total_digits <= b:
    total += i

print(total)
