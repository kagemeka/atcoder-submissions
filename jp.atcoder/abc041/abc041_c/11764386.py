import sys

n, *h = map(int, sys.stdin.read().split())
h = sorted(enumerate(h, start=1), key=lambda x: -x[1])

def main():
    for x in h:
        print(x[0])

if __name__ ==  '__main__':
    main()
