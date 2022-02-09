import typing
import itertools

def main() -> None:
    n = int(input())
    m = 2 * n
    a = [[0] * m for _ in range(m)]
    for i in range(2 * n - 1):
        a[i][i + 1:] = list(map(int, input().split()))

    mx = 0
    for comb in itertools.combinations(range(m - 1), n):
        comb = tuple(comb)
        s = (1 << m) - 1
        for i in comb:
            s &= ~(1 << i)
        pair = [i for i in range(m) if s >> i & 1]
        for perm in itertools.permutations(pair):
            tot = 0
            for x, y in zip(comb, pair):
                if x > y:
                    break
                tot ^= a[x][y]
            else:
                mx = max(mx, tot)
    print(mx)




if __name__ == "__main__":
    main()
