X = int(input())

n = int((2 * X)**0.5)
if n * (n + 1) >= 2 * X:
    ans = n
else:
    ans = n + 1

print(ans)
