import typing
import sys


def solve(x: int, y: int, a: typing.Tuple[int]) -> typing.NoReturn:
    n = len(a)

    def dfs(s: int, x: int, y: int) -> bool:
        if x < 0 or y < 0: return False
        if s == (1 << n) - 1: return True
        if x <= 0 or y <= 0: return False
        ok = False
        for i in range(n):
            if s >> i & 1: continue
            ok |= dfs(s | 1 << i, x, y - (a[i] + x - 1) // x)
            ok |= dfs(s | 1 << i, x - (a[i] + y - 1) // y, y)
        return ok

    print('Yes' if dfs(0, x, y) else 'No')



def main() -> typing.NoReturn:
    x, y, a, b, c = map(int, input().split())
    # a = np.array([a, b, c])
    a = (a, b, c)
    solve(x, y, a)


main()
