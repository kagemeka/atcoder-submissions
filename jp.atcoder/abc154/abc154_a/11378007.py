import sys

s, t = sys.stdin.readline().split()
a, b = map(int, sys.stdin.readline().split())
u = sys.stdin.readline().rstrip()

def main(a, b):
    if u == s: a -= 1
    else: b -= 1
    print(a, b)

if __name__ ==  '__main__':
    main(a, b)
