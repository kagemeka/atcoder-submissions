n = int(input())
t0, x0, y0 = 0, 0, 0
t, x, y = t0, x0, y0 # current
ans = "Yes"
for i in range(1, n+1):
  ti, xi, yi = map(int, input().split())
  displacement = (xi - x) + (yi - y)
  distance = abs(displacement)
  dt = ti - t
  # 時間差が移動距離より大きく、時間差-距離がeven_numberだったら
  # 寄り道しても往復してたどり着ける
  if dt >= distance and (dt - distance) % 2 == 0:
    t, x, y = ti, xi, yi
  else:
    ans = "No"
    break

print(ans)
