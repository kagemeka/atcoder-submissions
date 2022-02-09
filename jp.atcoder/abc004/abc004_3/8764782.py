import sys
n = int(sys.stdin.readline().rstrip())
n %= 30 # 30回で123456に戻る

def main():
    q, r = divmod(n, 5)

    res = []
    for i in range(q+2, 7):
        res.append(i)
    for i in range(1, q+1):
        res.append(i)

    res.insert(r, q+1)
    print(*res, sep='')

if __name__ == '__main__':
    main()
