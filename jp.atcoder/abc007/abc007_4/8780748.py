import sys

def ngCnt(n):
    all_cnt = n + 1
    n = str(n)
    l = len(n)

    ok_cnt = 0
    for i in range(l):
        d = int(n[i])
        if 0 <= d < 4:
            ok_cnt += d * 8 ** (l - (i + 1))
        elif d == 4:
            ok_cnt += 4 * 8 ** (l - (i + 1))
            break
        elif d < 9:
            ok_cnt += (d - 1) * 8 ** (l - (i + 1))
        else:
            ok_cnt += 8 * 8 ** (l - (i + 1))
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
