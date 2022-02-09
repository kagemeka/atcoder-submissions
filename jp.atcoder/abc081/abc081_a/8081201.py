ls = list(map(int, input().split()))
count = 0
for i in ls:
  if ls[i] == 1:
    count += 1
print(count)
