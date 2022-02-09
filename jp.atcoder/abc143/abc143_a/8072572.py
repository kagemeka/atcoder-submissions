a, b = map(int, input().split())

horizontal_length = b * 2

uncovered_part = a - horizontal_length

if uncovered_part > 0:
  return
else:
  uncovered_part = 0

print uncovered_part
