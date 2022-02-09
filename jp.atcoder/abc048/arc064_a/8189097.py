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
    while a[i] + a[i+1] > x:
        if a[i] > 0:
            a[i] -= 1
        else:
            a[i+1] -= 1
        count1 += 1

count2 = count
for i in range(n-1):
    while b[i] + b[i+1] > x:

        if b[i+1] > 0:
            b[i+1] -= 1
        else:
            b[i] -= 1
        count2 += 1

count = min(count1, count2)
print(count)
