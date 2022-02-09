import sys


def main():
    n, s = sys.stdin.read().split()

    # 左右から一度ずつチェック
    # 左から
    count = 0
    flag = False
    for i in range(len(s)):
        if s[i] == ')':
            if not flag:
                count += 1
            else:
                flag = False
                continue
        else:
            if not flag:
                flag = True
            else:
                break

    s = '(' * count + s

    # 右から
    count = 0
    flag = False
    for i in range(len(s)-1, -1, -1):
        if s[i] == '(':
            if not flag:
                count += 1
            else:
                flag = False
                continue
        else:
            if not flag:
                flag = True
            else:
                break

    s = s + ')' * count

    print(s)

if __name__ == "__main__":
    main()
