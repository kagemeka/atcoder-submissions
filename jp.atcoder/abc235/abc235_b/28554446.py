import typing


def main() -> None:
    n = int(input())
    h = list(map(int, input().split()))

    mx = 0
    for x in h:
        if x > mx:
            mx = x
        else:
            break
    print(mx)

main()
