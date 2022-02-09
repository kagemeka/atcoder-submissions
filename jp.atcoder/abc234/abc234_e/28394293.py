import typing


def main() -> None:
    x = input()
    # one digit -> answer
    # two digit -> answer
    # otherwize, the length will not changed (at last 99...99)

    l = len(x)
    if l <= 2:
        print(x)
        return

    # brute force first 2 digit
    a = list(map(int, x))
    for i in range(1, 10):
        if i < a[0]: continue
        for j in range(10):
            if i == a[0] and j < a[1]: continue
            delta = j - i
            b = [-1] * l
            b[0] = i
            b[1] = j
            flg = True
            for k in range(2, l):
                b[k] = b[k - 1] + delta
                if not 0 <= b[k] < 10:
                    flg = False
                    break
            if not flg: continue
            print(''.join(map(str, b)))
            return



main()
