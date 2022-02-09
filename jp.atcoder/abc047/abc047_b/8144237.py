W, H, N = map(int, input().split())
w, h = W, H

ll_ur = [0, w, 0, h]  # lower_left, upper_right corner

dic = dict(enumerate(ll_ur, 1))

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1 and dic[a] < x:
        dic[a] = x
    if a == 2 and dic[a] > x:
        dic[a] = x
    if a == 3 and dic[a] < y:
        dic[a] = y
    if a == 4 and dic[a] > y:
        dic[a] = y

if dic[1] < dic[2] and dic[3] < dic[4]:
    ans = (dic[2] - dic[1]) * (dic[4] - dic[3])
else:
    ans = 0

print(ans)
