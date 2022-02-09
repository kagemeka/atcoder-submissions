n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
count = 0
for i in a:
    if i > x:
        i = x
        count += i - x
b = a.copy()

count1 = count
for i in range(n-1):
    if a[i] + a[i+1] > x:
        d = a[i] + a[i+1] - x
        if a[i] >= d:
            a[i] -= d
        else:
            a[i] = 0
            a[i+1] -= d - a[i]
        count1 += d

count2 = count
for i in range(n-1):
    if b[i] + b[i+1] > x:
        d = b[i] + b[i+1] - x
        if b[i+1] >= d:
            b[i+1] -= d
        else:
            b[i+1] = 0
            b[i] -= d - b[i]
        count2 += d

count = min(count1, count2)
print(count)
