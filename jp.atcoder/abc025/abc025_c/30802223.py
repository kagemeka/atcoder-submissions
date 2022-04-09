import functools


def main() -> None:
    b = [0] * 6
    c = [0] * 8
    for i in range(2):
        row = list(map(int, input().split()))
        for j in range(3):
            b[i * 3 + j] = row[j]

    for i in range(3):
        row = list(map(int, input().split()))
        for j in range(2):
            c[i * 3 + j] = row[j]

    total_score = sum(b) + sum(c)

    def compute_chokudai_score(result_bits: int) -> int:
        s = 0
        for i in range(6):
            s += (result_bits >> i & 1 == result_bits >> (i + 3) & 1) * b[i]

        for i in range(8):
            s += (result_bits >> i & 1 == result_bits >> (i + 1) & 1) * c[i]
        return s

    @functools.lru_cache(maxsize=None)
    def dfs(result_bits: int, fixed_bits: int) -> int:
        popcount = sum(fixed_bits >> i & 1 for i in range(9))
        if popcount == 9:
            return compute_chokudai_score(result_bits)

        turn = popcount & 1  # 0 -> chokudai, t -> naoko

        final_scores = [
            dfs(result_bits | turn << i, fixed_bits | 1 << i)
            for i in range(9)
            if ~fixed_bits >> i & 1
        ]
        final_scores.sort(reverse=True)
        return final_scores[-turn]

    chokudai_score = dfs(0, 0)
    print(chokudai_score)
    print(total_score - chokudai_score)


if __name__ == "__main__":
    main()
