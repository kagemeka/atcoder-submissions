import sys
def main():
    n, q = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip()
    lr = map(int, sys.stdin.read().split())
    lr = list(zip(lr, lr))

    cumsum = [None] * (n + 1)
    cumsum[0] = 0

    flag = False
    for i in range(n):
        t = s[i]
        if t == 'A':
            flag = True
            cumsum[i+1] = cumsum[i]
        else:
            if t == 'C' and flag:
                cumsum[i+1] = cumsum[i] + 1
            else:
                cumsum[i+1] = cumsum[i]
            flag = False

    for l, r in lr:
        res = cumsum[r] - cumsum[l]
        print(res)

if __name__ == "__main__":
    main()
