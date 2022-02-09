import sys

a, b, c, k, s, t = map(int, sys.stdin.read().split())

def main():
    tot = a*s + b*t
    tot -= c * (s+t) if s + t >= k else 0
    print(tot)

if __name__ ==  '__main__':
    main()
