# 2019-11-23 18:41:55(JST)
import sys

def main():
    n, *ng = map(int, sys.stdin.read().split())
    ng.sort()
    if n in ng:
        print('NO')
        sys.exit()

    count = 0
    while n > 0:
        if not n - 3 in ng:
            n -= 3
            count += 1
        elif not n - 2 in ng:
            n -= 2
            count += 1
        elif not n - 1 in ng:
            n -= 1
            count += 1
        else:
            ans = 'NO'
            break
    else:
        if count > 100:
            ans = 'NO'
        else:
            ans = 'YES'

    print(ans)

if __name__ == '__main__':
    main()
