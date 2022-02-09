n, y = map(int, input().split())
y /= 1000
res10, res5, res1 = -1, -1, -1
for a in range(n+1):
  if res1 != -1:
    break
  for b in range(n-a+1):
    c = n - a - b
    total = 10000*a + 5000*b + 1000*c
    if total == y:
      res10, res5, res1 = a, b, c
    if res1 != -1:
      break
print(str(res10) + " " + str(res5) + " " + str(res1))
