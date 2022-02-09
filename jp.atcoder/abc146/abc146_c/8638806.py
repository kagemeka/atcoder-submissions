import sys

a, b, x = map(int, sys.stdin.readline().split())

def cost(n):
    return a * n + b * len(str(n))

l, r = 0, 10 ** 9
while l < r:
    m = (l + r) // 2
    c = cost(m)
    if c == x:
        print(m)
        sys.exit()
    elif cost(m) < x:
        l = m + 1
    else:
        r = m - 1

print(l)
# 直前の l = r - 1で、右側が最大だったらl+1だし、左が最大だったらlのまま
