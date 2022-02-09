import sys

def main():
    n, *a = map(int, sys.stdin.read().split())
    a.append(0)

    res = 0
    cnt = 1
    for i in range(n):
        if a[i] < a[i+1]:
            cnt += 1
        else:
            res += (1 + cnt) * cnt // 2
            cnt = 1
    print(res)

if __name__ == '__main__':
    main()
