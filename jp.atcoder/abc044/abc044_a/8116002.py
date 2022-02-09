n = int(input())
k = int(input())
x = int(input())
y = int(input())

ans = (k*x + (n-k)*y) if n >= k else n*x
print(ans)
