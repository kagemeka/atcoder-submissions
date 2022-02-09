import math

a, b, x = map(int, input().split())

sa = a ** 2
sb = a * b

if x / sa >= b / 2:
    y = ((b - x / sa) * 2) / a
    ans = math.atan(y) * 180 / math.pi
else:
    y = b / (2 * x / sb)
    ans = math.atan(y) * 180 / math.pi

print(ans)
