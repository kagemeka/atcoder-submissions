import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

def main():
    w = set()
    s = set()
    for i in range(0, f + 1, 100 * a):
        for j in range(0, f - i + 1, 100 * b):
            w.add(i + j)
    for i in range(0, f + 1, c):
        for j in range(0, f - i + 1, d):
            s.add(i + j)
    w = sorted(w)[1:]
    s = sorted(s)
    y = x = 0
    for i in w:
        for j in s:
            if i + j > f: break
            if j * (100 + e) > e * (i + j): break
            if (j * y >= x * (i + j)):
                y = i + j
                x = j
    print(y, x)

if __name__ ==  '__main__':
    main()
