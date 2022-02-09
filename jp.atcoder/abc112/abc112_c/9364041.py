import sys

n, *xyh = map(int, sys.stdin.read().split())
xyh = list(zip(*[iter(xyh)] * 3))

def conflict(cx, cy, ch, x, y, h):
    return h != max(ch - abs(x - cx) - abs(y - cy), 0)

def main():
    for x, y, h in xyh:
        if h >= 1:
            xt, yt, ht = x, y, h
            break

    for cx in range(101):
        for cy in range(101):
            ch = ht + abs(cx - xt) + abs(cy - yt)
            for x, y, h in xyh:
                if conflict(cx, cy, ch, x, y, h):
                    break
            else:
                return cx, cy, ch

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
