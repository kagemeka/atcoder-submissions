import sys

n, *a = map(int, sys.stdin.read().split())
a += [0]

def main():
    prev = 1001001001
    cnt = 0
    res = 0
    for x in a:
        if x <= prev:
            res += cnt * (cnt - 1) // 2 + cnt
            cnt = 1
        else:
            cnt += 1
        prev = x
    print(res)

if __name__ ==  '__main__':
    main()
