ls = list(map(int, input().split()))
count5, count7, ans = 0, 0, "NO"

for digit in ls:
    if digit == 5:
        count5 += 1
    elif digit == 7:
        count7 += 1

if count5 == 2 and count7 == 1:
    ans = "YES"

print(ans)
