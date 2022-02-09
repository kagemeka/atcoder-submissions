import sys

def main():
    a, b, x = map(int, sys.stdin.readline().split())

    if x >= a * 10 ** 9 + b * 10:
        print(10 ** 9)
        sys.exit()
    elif x < a + b:
        print(0)
        sys.exit()

    cand = []
    for d in range(1, 10):
        n = (x - b * d) // a
        # d(n) must be l
        if 10 ** (d - 1) <= n < 10 ** d:
            cand.append(n)
        elif n >= 10 ** d:
            n = 10 ** d - 1
            cand.append(n)
        # if n < 10 ** (l - 1), it's impossible d(n) == d.

    print(cand[-1])

if __name__ == '__main__':
    main()
