import typing


def main() -> None:
    n = int(input())
    N = 360
    cut = [False] * (N + 1)
    a = list(map(int, input().split()))
    i = 0
    cut[i] = True
    cut[i + N] = True
    for d in a:
        i = (i - d) % N
        cut[i] = True
    mx = 0
    prev = 0
    for i in range(1, N + 1):
        if cut[i]:
            mx = max(mx, i - prev)
            prev = i

    print(mx)


if __name__ == "__main__":
    main()
