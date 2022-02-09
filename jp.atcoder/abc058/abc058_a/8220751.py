a, b, c = [int(_) for _ in input().split()]
if b - a == c - b:
    ans = "YES"
else:
    ans = "NO"

print(ans)
