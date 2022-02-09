import sys


def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    for i in range(n):
        if s[i] == ')':
            continue
        else:
            i_l = i
            break
    for i in range(n, 0, -1):
        if s[i-1] == '(':
            continue
        else:
            i_r = i
            break
    res_l = '(' * len(s[:i_l]) + s[:i_l]
    res_r = s[i_r:] + ')' * len(s[i_r:])

    c = s[i_l:i_r]
    count = c.count('(') - c.count(')')
    if count == 0:
        ans = res_l + c + res_r
    elif count < 0:
        ans = '(' * abs(count) + res_l + c + res_r
    else:
        ans = res_l + c + res_r + ')' * count
    print(ans)
    # s = '.' + s

    # # 左右から一度ずつチェック
    # # 左から
    # count = 0
    # flag = False
    # for i in range(1, len(s)):
    #     if s[i] == ')':
    #         if not flag:
    #             count += 1
    #         else:
    #             flag = False
    #     elif s[i] == '(':
    #         if s[i-1] == '.':
    #             count -= 1
    #         elif s[i-1] == ')':
    #             flag = True
    #         elif s[i-1] == '(':
    #             if not flag:
    #                 count -= 1
    #             else:
    #                 break

    # s = s.replace('.', '') + '.'
    # if count >= 1:
    #     s = '(' * count + s


    # count = 0
    # flag = False
    # for i in range(len(s)-2, -1, -1):
    #     if s[i] == '(':
    #         if not flag:
    #             count += 1
    #         else:
    #             flag = False
    #     elif s[i] == ')':
    #         if s[i+1] == '.':
    #             count -= 1
    #         elif s[i+1] == '(':
    #             flag = True
    #         elif s[i+1] == ')':
    #             if not flag:
    #                 count -= 1
    #             else:
    #                 break
    #     print(count)

    # s = s.replace('.', '')
    # if count >= 1:
    #     s = s + ')' * count

    # print(s)



if __name__ == "__main__":
    main()
