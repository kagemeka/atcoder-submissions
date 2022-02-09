import bisect
n = int(input())

li = list(map(int, input().split()))
li.sort()

count = 0

for i in range(n - 2):
  for j in range(i + 1, n - 1):
    bi = bisect.bisect_left(li, li[i] + li[j])
    count += bi - j - 1
print(count)
