# 2019-11-27 14:53:01(JST)
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    code = sys.stdin.read().split()

    cnt = 0
    flag = False
    for j in range(9):
        for i in range(n):
            current = code[i][j]
            if flag and current != 'o':
                cnt += 1
                flag = False
            elif not flag and current == 'o':
                flag = True

            if current == 'x':
                cnt += 1
        if flag:
            cnt += 1
            flag = False

    print(cnt)

if __name__ == '__main__':
    main()
