import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    x = int(n / 1.08) # 切り捨て

    res = []
    while x * 27 // 25 == n:
        res.append(x)
        x += 1
    if res:
        print(res[0])
    else:
        print(':(')

if __name__ == '__main__':
    main()
