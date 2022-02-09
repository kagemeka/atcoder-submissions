import sys


def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    left, right = 0, 0
    for char in s:
        if char == '(':
            right += 1
            # prefixが')'の可能性があるのでleftを削ることはできない
        elif char == ')':
            if right:
                # rightがあるならこれより前に必ず'('が存在するのでrightの可能性を一つ削ってこれを代わりにその'('とペアにする
                right -= 1
            else: # rightがない場合はこれとペアになることのできる'('がこれ以前に出現していないということので追加
                left += 1

    ans = '(' * left + s + ')' * right
    print(ans)


if __name__ == "__main__":
    main()
