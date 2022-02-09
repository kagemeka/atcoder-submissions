n = int(input())
a = [int(a) for a in input().split()]

def f(times, prefix_sum):
    for i in range(1, n):
        if prefix_sum < 0:
            if prefix_sum + a[i] > 0:
                prefix_sum += a[i]
            else:
                times += 1 - (prefix_sum + a[i])
                prefix_sum = 1
        elif prefix_sum > 0:
            if prefix_sum + a[i] < 0:
                prefix_sum += a[i]
            else:
                times += abs(-1 - (prefix_sum + a[i]))
                prefix_sum = -1

    return times

if a[0] > 0:
    t1 = 0
    p1 = a[0]
else:
    t1 = 1 - a[0]
    p1 = 1


if a[0] < 0:
    t2 = 0
    p2 = a[0]
else:
    t2 = abs(-1 - a[0])
    p2 = -1


print(min(f(t1, p1), f(t2, p2)))
