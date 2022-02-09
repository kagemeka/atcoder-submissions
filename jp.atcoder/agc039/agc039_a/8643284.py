# 2019-11-25 06:26:24(JST)
import sys

def main():
    s, k = sys.stdin.read().split()
    k = int(k)

    if s.count(s[0]) == len(s):
        if len(s) % 2 == 0:
            ans = len(s) // 2 * k
        else:
            if k % 2 == 0:
                ans = len(s) * (k // 2)
            else:
                ans = len(s) * (k // 2) + len(s) // 2
        print(ans)
        sys.exit()

    count = 0
    same = 1
    flag = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            same += 1
        else:
            if not flag:
                first_same = same
                flag = True
                # 最初に何文字連続するかだけ記録しておく
                # (最初と最後の文字が同じだった場合の処理のため)
            count += same // 2
            same = 1

    bl = False
    if s[-1] == s[0]:
        if same % 2 == 1 and first_same % 2 == 1:
            # ここでのsameは一番最後に連続した文字数
            count += same // 2 + 1
            # この場合は最後だけ調整が必要なので記録しておく
            bl = True
        else:
            count += same // 2
    else:
        count += same // 2

    ans = count * k
    if bl:
        ans -= 1

    print(ans)

if __name__ == '__main__':
    main()
