import typing
import bisect


def main() -> typing.NoReturn:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if l[i] == l[j]: continue
            for k in range(j + 1, n):
                if l[j] == l[k]: continue
                if l[k] >= l[i] + l[j]: break
                cnt += 1
    print(cnt)


main()
