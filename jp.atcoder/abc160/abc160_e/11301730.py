import sys

x, y, a, b, c = map(int, sys.stdin.readline().split())
*p, = map(int, sys.stdin.readline().split())
*q, = map(int, sys.stdin.readline().split())
*r, = map(int, sys.stdin.readline().split())

def main():
    cnt = [0] * 3
    cand = []
    for i in p:
        cand.append((i, 0))
    for i in q:
        cand.append((i, 1))
    for i in r:
        cand.append((i, 2))
    cand.sort()

    tot = 0
    res = 0
    for _ in range(a+b+c):
        d, k = cand.pop()
        if k == 0:
            if cnt[0] == x:
                continue
            cnt[0] += 1
            res += d
            tot += 1
        elif k == 1:
            if cnt[1] == y:
                continue
            cnt[1] += 1
            res += d
            tot += 1
        elif k == 2:
            cnt[2] += 1
            res += d
            tot += 1
        if tot == x + y:
            break

    print(res)

if __name__ == "__main__":
    main()
