import typing


def main() -> None:
    h, w = map(int, input().split())

    s = [input() for _ in range(h)]

    p = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == "-":
                continue
            p.append((i, j))

    x, y = p[0]
    a, b = p[1]
    print(abs(x - a) + abs(y - b))


if __name__ == "__main__":
    main()
