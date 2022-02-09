n, a, b = map(int, input().split())
total = 0

def sum_digits(digits):
  return sum(int(digit) for digit in str(digits))

for i in range(1, n+1):
  if sum_digits(i) >= a and sum_digits(i) <= b:
    total += i

print(total)
