n = int(input())
s = input()

ans = 1
current = s[0]
for i in range(n):
  if current != s[i]:
    ans += 1
    current = s[i]
print ans
