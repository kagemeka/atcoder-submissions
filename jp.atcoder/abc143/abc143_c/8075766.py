n = int(input())
s = input()
i = 0
while i < n - 1:
  
  while s[i + 1] and s[i] == s[i + 1]:
    s.pop(i + 1)
    n -= 1
  i += 1
print(n)
