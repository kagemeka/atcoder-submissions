import typing
import itertools

def main() -> None:
    n = int(input())
    m = 2 * n
    a = [[0] * m for _ in range(m)]
    for i in range(m - 1):
        a[i][i + 1:] = list(map(int, input().split()))

    if n == 1:
        print(a[0][1])
        return
    mx = 0
    for comb in itertools.combinations(range(m - 2), n - 1):
        left = [0]
        for x in comb:
            left.append(x + 1)
        assert len(left) == n
        s = (1 << m) - 1
        for i in left:
            s &= ~(1 << i)
        right = [i for i in range(m) if s >> i & 1]
        assert len(right) == n
        flg = True
        for x, y in zip(left, right):
            if x > y:
                flg = False
                break
        if not flg:
            continue
        for perm in itertools.permutations(right):
            tot = 0
            for x, y in zip(left, perm):
                if x > y:
                    break
                tot ^= a[x][y]
            else:
                mx = max(mx, tot)
    print(mx)


if __name__ == "__main__":
    main()
