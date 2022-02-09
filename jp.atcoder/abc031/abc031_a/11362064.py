import sys

a, d = map(int, sys.stdin.readline().split())

def main(a, d):
    if a <= d: a += 1
    else: d += 1
    print(a * d)

if __name__ ==  '__main__':
    main(a, d)
