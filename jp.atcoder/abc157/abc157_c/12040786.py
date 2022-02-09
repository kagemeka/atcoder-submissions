import sys

n, m, *sc = map(int, sys.stdin.read().split())
sc = zip(*[iter(sc)] * 2)

def main():
    a = [0] * n
    b = [0] * n
    for s, c in sc:
        s -= 1
        if b[s] and a[s] != c:
            print(-1); return
        elif s == c == 0 and n > 1:
            print(-1); return
        b[s] = 1
        a[s] = c
    if not b[0] and n > 1: a[0] = 1
    print(''.join(map(str, a)))

if __name__ ==  '__main__':
    main()
