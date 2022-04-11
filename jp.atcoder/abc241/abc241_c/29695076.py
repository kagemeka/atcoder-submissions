import typing


def main() -> None:
    n = int(input())
    s = [input() for _ in range(n)]

    k = 6

    def contains_4(s: typing.List[str]) -> bool:
        for y in range(n - k + 1):
            for x in range(n - k + 1):
                if s[y][x : x + k].count("#") >= 4:
                    return True
                cnt = 0
                for d in range(k):
                    cnt += s[y + d][x + d] == "#"
                if cnt >= 4:
                    return True
        return False

    if contains_4(s):
        print("Yes")
        return

    t = [["."] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t[j][i] = s[i][j]
    t = t[::-1]
    # for row in t:
    #     print(row)
    if contains_4(t):
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
