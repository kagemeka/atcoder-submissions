n = int(input())
s = input()
slimes = s.split("")
i = 0
while i < n - 1:
  s = slimes[i]
  while s == slimes[i+1]:
    del slimes[i+1]
    n -= 1
  i += 1
print n
