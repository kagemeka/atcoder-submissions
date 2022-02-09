n, y = map(int, input().split())
res10000, res5000, res1000 = -1, -1, -1
for i in range(n+1):
  if res10000 != -1:
    break
  for j in range(n-i+1):
    a = i
    b = j
    c = n - a - b
    total = 10000*a + 5000*b + 1000*c
    if total == y:
      res10000, res5000, res1000 = a, b, c

    if res10000 != -1:
      break

print(str(res10000) + " " + str(res5000) + " " + str(res1000))
