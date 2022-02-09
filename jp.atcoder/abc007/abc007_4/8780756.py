import sys

def ngCnt(n):
    all_cnt = n + 1
    n = str(n)
    l = len(n)

    ok_cnt = 0
    for i in range(l):
        d = int(n[i])
        if d <= 4:
            ok_cnt += d * 8 ** (l - (i + 1))
            if d == 4:
                break
        else:
            ok_cnt += (d - 1) * 8 ** (l - (i + 1))
            if d == 9:
                break
    else:
        ok_cnt += 1

    return all_cnt - ok_cnt

def main():
    l, r = map(int, sys.stdin.readline().split())
    ans = ngCnt(r) - ngCnt(l-1)
    print(ans)

if __name__ == '__main__':
    main()
