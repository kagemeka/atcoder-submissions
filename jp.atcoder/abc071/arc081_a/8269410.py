from sys import stdin

n, *a = map(int, stdin.read().split())
a.sort(reverse=1)

l_count = {}
for l in a:
    l_count.update({l: l_count.get(l, 0) + 1})

long_side, short_side = 0, 0
for l, c in sorted(l_count.items(), reverse=1):
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
