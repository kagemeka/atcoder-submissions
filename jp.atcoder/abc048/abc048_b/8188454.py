a, b, x = map(int, input().split())

if x > b:
    ans = 0
elif a <= x:
    ans = b // x
else :
    ans = b // x - (a - 1) // x

if a == 0:
    ans += 1

print(ans)
