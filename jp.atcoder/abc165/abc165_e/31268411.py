def main() -> None:
    n, m = map(int, input().split())
    # consider (a_i, b_i) 0 <= i < m in modular-n space.
    # when \forall{i}(b_i - a_i) -> {c_i},
    # {c_i} \land {-c_i} should be empty set.

    # example
    # n = 8, m = 3 -> {1, 2, 3} -> {-1, -2, -3} -> {7, 6, 5}
    # {1, 2, 3} & {5, 6, 7} = {}
    # (1, 8), (2, 4), (3, 6)

    print(1, n)
    for i in range(2, m + 1):
        print(i, i * 2)


if __name__ == "__main__":
    main()
