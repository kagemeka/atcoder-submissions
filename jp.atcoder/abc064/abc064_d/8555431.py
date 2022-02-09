import sys


def main():
    n, s = sys.stdin.read().split()

    s = '.' + s

    # 左右から一度ずつチェック
    # 左から
    count = 0
    flag = False
    for i in range(1, len(s)):
        if s[i] == ')':
            if not flag:
                count += 1
            else:
                flag = False
        elif s[i] == '(':
            if s[i-1] == '.':
                count -= 1
            elif s[i-1] == ')':
                flag = True
            elif s[i-1] == '(':
                if not flag:
                    count -= 1
                else:
                    break

    s = s.replace('.', '') + '.'
    if count >= 1:
        s = '(' * count + s


    count = 0
    flag = False
    for i in range(len(s)-2, -1, -1):
        if s[i] == '(':
            if not flag:
                count += 1
            else:
                flag = False
        elif s[i] == ')':
            if s[i-1] == '.':
                count -= 1
            elif s[i-1] == '(':
                flag = True
            elif s[i-1] == ')':
                if not flag:
                    count -= 1
                else:
                    break

    s = s.replace('.', '')
    if count >= 1:
        s = s + ')' * count

    print(s)



if __name__ == "__main__":
    main()
