import bisect

n = int(input())
ls = list(map(int, input().split()))
ls.sort()

count = 0

for i in range(n - 2):
  a = ls[i]
  for j in range(i + 1, n - 1):
    b = ls[j]
    index = bisect.bisect_left(ls, a + b):
    count += index - j - 1
print(count)
