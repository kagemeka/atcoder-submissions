# 2019-11-25 23:19:34(JST)
import sys

def main():
    n, *c = map(int, sys.stdin.read().split())

    # 自身を含めての自身の約数が何個あるか
    cnt = [sum(x % y == 0 for y in c) for x in c] # Trueは1としてカウントされる

    # 並べ変えた時に左側にある約数の個数が偶数だったら表になる
    # つまり自身の位置が約数の中で左から奇数番目になる確率が、表になる確率に等しい。
    # 約数が奇数個の場合と偶数個の場合で場合わけする。
    ans = sum(((x + 1) // 2) / x if x & 1 else 1 / 2 for x in cnt)
    print(ans)

if __name__ == '__main__':
    main()
