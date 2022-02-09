import sys

n = int(sys.stdin.readline().rstrip())

def main():
    res = [0, 0, 0]
    r = n
    for i in range(2, -1, -1):
        q, r = divmod(r, 60 ** i)
        res[i] = q

    if res[0] >= 24:
        res = [23, 59, 59]

    for i in range(3):
        if res[i] < 10:
            res[i] = '0' + str(res[i])
        else:
            res[i] = str(res[i])

    ans = ':'.join(res)
    print(ans)

if __name__ == '__main__':
    main()
