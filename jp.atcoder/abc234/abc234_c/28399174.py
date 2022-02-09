import typing


def main() -> None:
    k = int(input())

    a = []
    while k:
        if k & 1:
            a.append(2)
        else:
            a.append(0)
        k >>= 1

    print(''.join(map(str, a))[::-1])




main()
