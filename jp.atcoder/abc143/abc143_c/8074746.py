n = int(input())
s = input()
slimes = list(s)
i = 0
while i < n - 1:
  s = slimes[i]
  while s == slimes[i + 1]:
    slimes.pop(i + 1)
    n -= 1
  i += 1
print(n)
