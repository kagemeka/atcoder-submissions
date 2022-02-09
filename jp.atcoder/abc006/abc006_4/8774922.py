import sys

n, *c = map(int, sys.stdin.read().split())

def main():
    maximum = c[0]
    cnt1 = 0
    for i in range(1, n):
        if c[i] < maximum:
            cnt1 += 1
        else:
            maximum = c[i]

    minimum = c[-1]
    cnt2 = 0
    for i in range(n - 2, -1, -1):
        if c[i] > minimum:
            cnt2 += 1
        else:
            minimum = c[i]


    print(min(cnt1, cnt2))

if __name__ == '__main__':
    main()
