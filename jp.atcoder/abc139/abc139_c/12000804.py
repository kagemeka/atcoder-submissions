import sys

n, *h = map(int, sys.stdin.read().split())
h += [float('inf')]

def main():
    prev = res = cnt = 0
    for x in h:
        if x > prev:
            res = max(res, cnt)
            cnt = 0
        else:
            cnt += 1
        prev = x
    print(res)

if __name__ ==  '__main__':
    main()
