import sys
input = sys.stdin.readline

h, w = [int(x) for x in input().split()]

if h % 3 == 0 or 2 % 3 == 0:
    print(0)
    exit()

if h % 3 == 1:
    d = h // 3
else:
    d = h // 3 + 1
block = [w * d, (h-d) * (w // 2), (h-d) * (w - w // 2)]
for b in block:
    if b == int(b**0.5) ** 2:
        break
else:
    res1 = max(block) - min(block)

if w % 3 == 1:
    d = w // 3
else:
    d = w // 3 + 1
block = [h * d, (w-d) * (h // 2), (w-d) * (h - h // 2)]
for b in block:
    if b == int(b**0.5) ** 2:
        break
else:
    res2 = max(block) - min(block)

print(min(res1, res2))
