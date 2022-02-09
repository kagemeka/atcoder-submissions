w, a, b = [int(x) for x in input().split()]


if abs(a - b) > w:
    ans = abs(a - b) - w
else:
    ans = 0

print(ans)
