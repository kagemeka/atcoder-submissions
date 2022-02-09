import typing



def main() -> typing.NoReturn:
    '''
    (1 * n + 2 * (n - 1) + ... + (n - 1) * 2 + n * 1) - \sum_{edge} {disconnect count}
    '''

    n = int(input())
    cnt = 0
    for i in range(n):
        cnt += (i + 1) * (n - i)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if u > v: u, v = v, u
        cnt -= u * (n - v + 1)
    print(cnt)

main()
