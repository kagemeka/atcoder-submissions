a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      total = 500*i + 100*j + 50*k
      if total == x:
        count += 1
print(count)
