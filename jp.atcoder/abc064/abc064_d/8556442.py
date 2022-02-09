import sys


def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    left, right = 0, 0
    for char in s:
        if char == '(':
            right += 1
            # これ以前に出現している')'の数が'('の数より多い可能せがあるのでleftを削ることはできないため、ペアになる可能性としての')'を追加
        elif char == ')':
            if right:
                # rightがあるならこれより前に必ずペア未確定の'('が存在するのでrightの可能性を一つ削ってこれを代わりにその'('とペアにする
                right -= 1
            else:
                # rightがない場合はペア未確定の'('がこれ以前に出現していないということので'('を追加してこれとペアにするしかない
                left += 1

    ans = '(' * left + s + ')' * right
    print(ans)


if __name__ == "__main__":
    main()
