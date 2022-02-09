import sys

a, b, x = map(int, sys.stdin.readline().split())

def main():
    if x >= a * 10 ** 9 + b * 10:
        print(10 ** 9)
        return
    elif x < a + b:
        print(0)
        return

    ans = 0
    for d in range(1, 10):
        n = (x - b * d) // a
        if len(str(n)) < d: continue
        ans = max(ans, min(n, 10**d-1))
    print(ans)

if __name__ ==  '__main__':
    main()
