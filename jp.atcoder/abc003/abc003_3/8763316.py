import sys

n, k, *r = map(int, sys.stdin.read().split())
r.sort()
cand = r[-k:]

def main():
    rate = 0
    for c in cand:
        if rate < c:
            rate = (rate + c) / 2

    print(rate)

if __name__ == '__main__':
    main()
