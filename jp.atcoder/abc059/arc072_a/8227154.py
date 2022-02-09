n = int(input())
a = [int(a) for a in input().split()]

times = 0
previous = a[0]
for i in range(1, n):
    if previous < 0:
        if previous + a[i] > 0:
            previous = previous + a[i]
        else:
            times += 1 - (previous + a[i])
            previous = 1
    elif previous > 0:
        if previous + a[i] < 0:
            previous = previous + a[i]
        else:
            times += abs(-1 - (previous + a[i]))
            previous = -1
print(times)
