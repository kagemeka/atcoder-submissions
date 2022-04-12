def popcount(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def main() -> None:
    n, m = map(int, input().split())
    base_score = list(map(int, input().split()))

    bonus_score = []
    bonus_members = [0] * m
    for j in range(m):
        b, _, *members = map(int, input().split())
        bonus_score.append(b)
        for i in members:
            bonus_members[j] |= 1 << (i - 1)

    mx = 0
    for members in range(1 << n):
        if popcount(members) != 9:
            continue
        score = 0
        for i in range(n):
            if ~members >> i & 1:
                continue
            score += base_score[i]

        for i in range(m):
            if popcount(members & bonus_members[i]) >= 3:
                score += bonus_score[i]
        mx = max(mx, score)
    print(mx)


if __name__ == "__main__":
    main()
