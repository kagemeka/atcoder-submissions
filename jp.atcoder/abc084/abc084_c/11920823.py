import sys

n, *csf = map(int, sys.stdin.read().split())
csf = list(zip(*[iter(csf)] * 3))

def main():
    for i in range(n - 1):
        t = 0
        for c, s, f in csf[i:]:
            if t <= s: t = s + c
            else: t = s + ((t - s + f - 1) // f) * f + c
        print(t)
    print(0)

if __name__ ==  '__main__':
    main()
