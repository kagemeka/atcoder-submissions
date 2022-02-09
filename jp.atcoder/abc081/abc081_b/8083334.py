n = int(input())
a = list(map(int, input().split()))
count = 0
only_even = True
while only_even:
  for i in range(n):
    if a[i] % 2 != 0:
      only_even = False

  if only_even == False:
    break

  for i in range(n):
    a[i] /= 2
  count += 1

print(count)
