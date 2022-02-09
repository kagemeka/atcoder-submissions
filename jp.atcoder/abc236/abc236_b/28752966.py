import typing


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    for x in a:
        cnt[x - 1] += 1
    for i in range(n):
        if cnt[i] == 4:
            continue
        print(i + 1)
        return


if __name__ == "__main__":
    main()
