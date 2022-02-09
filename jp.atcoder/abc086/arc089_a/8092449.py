n = int(input())
t, x, y = 0, 0, 0
ans = "Yes"
for i in range(1, n+1):
  ti, xi, yi = map(int, input().split())
  displacements = (xi - x) + (yi - y)
  dist = abs(displacements)
  dt = ti - t
  if dt >= dist and (dt - dist) % 2 == 0:
    t, x, y = ti, xi, yi
  else:
    ans = "No"

print(ans)
