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
res1 = max(block) - min(block)
block = [w * d, w * d, w * (h - d * 2)]
res2 = max(block) - min(block)

if w % 3 == 1:
    d = w // 3
else:
    d = w // 3 + 1
block = [h * d, (w-d) * (h // 2), (w-d) * (h - h // 2)]
res3 = max(block) - min(block)
block = [h * d, h * d, h * (w - d * 2)]
res4 = max(block) - min(block)

print(min(res1, res2, res3, res4))
