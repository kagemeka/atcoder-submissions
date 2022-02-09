# c_WA2.py よりはWAが減った

n = int(input())
a = [int(a) for a in input().split()]

times = 0
sum_prefix = a[0]
for i in range(1, n):
    if sum_prefix < 0:
        if sum_prefix + a[i] > 0:
            sum_prefix += a[i]
        else:
            times += 1 - (sum_prefix + a[i])
            sum_prefix = 1
    elif sum_prefix > 0:
        if sum_prefix + a[i] < 0:
            sum_prefix += a[i]
        else:
            times += abs(-1 - (sum_prefix + a[i]))
            sum_prefix = -1


times2 = 0
if a[0] > 0:
    times2 += abs(-1 - a[0])
    sum_prefix = -1
else:
    times2 += 1 - a[0]
    sum_prefix = 1
for i in range(1, n):
    if sum_prefix < 0:
        if sum_prefix + a[i] > 0:
            sum_prefix = sum_prefix + a[i]
        else:
            times2 += 1 - (sum_prefix + a[i])
            sum_prefix = 1
    elif sum_prefix > 0:
        if sum_prefix + a[i] < 0:
            sum_prefix = sum_prefix + a[i]
        else:
            times2 += abs(-1 - (sum_prefix + a[i]))
            sum_prefix = -1

print(min(times, times2))
