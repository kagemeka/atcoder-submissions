def main() -> None:
    n = int(input())
    strings = [input() for _ in range(n)]
    target = "AB"
    count = sum(s.count(target) for s in strings)
    tail_a = 0
    head_b = 0
    both = 0
    for s in strings:
        tail_a += s[-1] == "A"
        head_b += s[0] == "B"
        both += s[-1] == "A" and s[0] == "B"

    count += min(tail_a, head_b)
    count -= tail_a == head_b == both >= 1
    print(count)


if __name__ == "__main__":
    main()
