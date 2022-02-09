import sys


x = int(sys.stdin.readline().rstrip())
def main():
    y = 100
    cnt = 0
    while True:
        y = y * 1.01 // 1
        cnt += 1
        if y >= x:
            print(cnt)
            return
if __name__ == '__main__':
    main()
