n, a, b = map(int, input().split())
total = 0
for i in range(1, n+1):
  total_digit = 0
  j = i
  while j > 0:
    total_digit += j % 10
    j //= 10
    if j == 0:
      if total_digit >= a and total_digit <= b:
        total += i
      break

print(total)
