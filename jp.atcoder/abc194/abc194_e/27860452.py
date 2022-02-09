import typing


def main() -> typing.NoReturn:
    n, m =  map(int, input().split())
    a = list(map(int, input().split()))
    indices = [[-1, n] for _ in range(n)]
    for i in range(n):
        indices[a[i]].append(i)

    for x in range(n):
        b = indices[x]
        b.sort()
        for i in range(len(b) - 1):
            if b[i + 1] - b[i] <= m: continue
            print(x)
            return
    print(n)

main()
