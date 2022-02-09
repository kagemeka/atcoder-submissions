from sys import stdin

n, *a = map(int, stdin.read().split())
lengths = sorted(set(a), reverse=1)
a.sort()

long_side, short_side = 0, 0
for l in lengths:
    c = a.count(l)
    if c != 1:
        if not long_side:
            if c >= 4:
                print(l ** 2)
                exit()
            else:
                long_side = l
        else:
            short_side = l
            break

print(long_side * short_side)
