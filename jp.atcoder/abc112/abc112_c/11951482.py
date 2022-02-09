import sys

n, *xyh = map(int, sys.stdin.read().split())
xyh = list(zip(*[iter(xyh)] * 3))

def contradict(cx, cy, ch, x, y, h):
    return max(ch - abs(x - cx) - abs(y - cy), 0) != h

def main():
    for x, y, h in xyh:
        if h: x0, y0, h0 = x, y, h; break
    cand = []
    for cx in range(101):
        for cy in range(101):
            ch = h0 + abs(cx - x0) + abs(cy - y0)
            for x, y, h in xyh:
                if contradict(cx, cy, ch, x, y, h): break
            else:
                cand.append((ch, cx, cy))
    cand.sort(reverse=True)
    res = cand[0]
    print(res[1], res[2], res[0])

if __name__ ==  '__main__':
    main()