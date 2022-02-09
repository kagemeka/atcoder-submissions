n = int(input())
a = [int(a) for a in input().split()]

previous = a[0]
for i in range(1, n):
    if previous < 0:
        if previous + a[i] > 0:
            previous = previous + a[i]
        else:
            break
    elif previous > 0:
        if previous + a[i] < 0:
            previous = previous + a[i]
        else:
            break
else:
    print(0)
    exit()

times1 = 0
times2 = 0
if a[0] < 0:
    times1 += abs(1 + abs(a[0]) - a[1])
    times2 += 1 - a[0] + abs(-2 - a[1])
    for i in range(3, n+1):
        if i % 2 != 0:
            times1 += abs(-2 - a[i-1])
            times2 += abs(2 - a[i-1])
        else:
            times1 += abs(2 - a[i-1])
            times2 += abs(-2 - a[i-1])
else:
    times1 += abs(-(1 + a[0]) - a[1])
    times2 += abs(-1 - a[0]) + abs(2 - a[1])
    for i in range(3, n+1):
        if i % 2 != 0:
            times1 += abs(2 - a[i-1])
            times2 += abs(-2 - a[i-1])
        else:
            times1 += abs(-2 - a[i-1])
            times2 += abs(2 - a[i-1])

print(min(times1, times2))
