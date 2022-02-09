from sys import stdin

n, *a = map(int, stdin.read().split())
lengths = sorted(set(a), reverse=1)
a.sort()

remainder = 4
long_side, short_side = 0, 0
for l in lengths:
    th = a.index(l)
    c = len(a) - th
    if c != 1:
        if remainder == 4:
            if c >= 4:
                print(l ** 2)
                exit()
            else:
                remainder = 2
                long_side = l
        else:
            short_side = l
            break
    a = a[:th]

print(long_side * short_side)
