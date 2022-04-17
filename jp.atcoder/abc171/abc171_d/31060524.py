def main() -> None:
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    s = sum(a)
    K = 1 << 17
    count = [0] * K
    for x in a:
        count[x] += 1

    q = int(input())
    for _ in range(q):
        b, c = map(int, input().split())
        s += (c - b) * count[b]
        print(s)
        count[c] += count[b]
        count[b] = 0


if __name__ == "__main__":
    main()
