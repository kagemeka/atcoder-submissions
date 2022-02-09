n = int(input())
s = input()
i = 0
while i < n - 1:
  s = s[i]
  if s[i + 1]:
    while s == s[i + 1]:
      s.pop(i + 1)
      n -= 1
  i += 1
print(n)
