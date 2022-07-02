# / mypy: ignore-errors
import typing


def main() -> None:
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]

    mx = 0
    for y in range(n):
        for x in range(n):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    v = 0
                    if dy == dx == 0:
                        continue
                    for k in range(n):
                        i = y + dy * k
                        j = x + dx * k
                        i %= n
                        j %= n
                        v = v * 10 + a[i][j]
                    mx = max(mx, v)
    print(mx)


main()
