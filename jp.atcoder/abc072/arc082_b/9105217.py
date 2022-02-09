import sys

n, *p = map(int, sys.stdin.read().split())

def main():
    res = 0
    cnt = 0
    for i in range(n):
        if p[i] == i + 1:
            cnt += 1
        else:
            if cnt == 1:
                res += 1
            elif cnt >= 2:
                res += cnt - 1
            cnt = 0
    if cnt == 1:
        res += 1
    elif cnt >= 2:
        res += cnt - 1

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
