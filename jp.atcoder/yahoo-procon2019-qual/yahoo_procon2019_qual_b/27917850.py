import typing

def main() -> typing.NoReturn:
    # n = 3
    deg = [0] * 4
    for _ in range(3):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        deg[a] += 1
        deg[b] += 1

    print('YES' if all(1 <= x <= 2 for x in deg) else 'NO')

main()
