import sys

m, *ng = map(int, sys.stdin.read().split())
ng = set(ng)

def main():
    n = m
    if n in ng:
        ans = 'NO'
    else:
        for _ in range(100):
            if not n - 3 in ng:
                n -= 3
            elif not n - 2 in ng:
                n -= 2
            elif not n - 1 in ng:
                n -= 1
            else:
                ans = 'NO'
                break

            if n <= 0:
                ans = 'YES'
                break
        else:
            ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
