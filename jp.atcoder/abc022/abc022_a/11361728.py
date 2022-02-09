import sys

n, s, t, w, *a  = map(int, sys.stdin.read().split())

def main():
    cur = w
    cnt = 1 if s <= cur <= t else 0
    for dw in a:
        cur += dw
        if s <= cur <= t: cnt += 1
    print(cnt)

if __name__ ==  '__main__':
    main()
