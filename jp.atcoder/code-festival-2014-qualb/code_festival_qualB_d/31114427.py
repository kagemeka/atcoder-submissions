import typing


def main() -> None:
    n = int(input())
    h = [int(input()) for _ in range(n)]

    def count_up(h: typing.List[int]) -> typing.List[int]:
        count = [0] * n
        INF = 1 << 60
        st = [(-1, INF)]
        for i in range(n):
            while st[-1][1] <= h[i]:
                st.pop()
            count[i] = i - st[-1][0] - 1
            st.append((i, h[i]))
        return count

    count = [0] * n
    for i, c in enumerate(count_up(h)):
        count[i] += c
    for i, c in enumerate(count_up(h[::-1])):
        count[n - i - 1] += c
    print(*count, sep="\n")


if __name__ == "__main__":
    main()
