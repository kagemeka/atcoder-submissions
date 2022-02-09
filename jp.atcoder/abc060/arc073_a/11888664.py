import sys

n, T, *t = map(int, sys.stdin.read().split())

def main():
    pushed = t[0]
    tot = 0
    for x in t[1:]:
        tot += min(T, x - pushed)
        pushed = x
    tot += T
    print(tot)

if __name__ ==  '__main__':
    main()
