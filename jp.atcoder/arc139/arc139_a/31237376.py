def main() -> None:
    n = int(input())
    t = list(map(int, input().split()))
    # greedy

    K = 60
    a = [1 << t[0]]
    for i in t[1:]:
        x = a[-1]
        a.append(x + 1 << i)
        for j in range(i, K):
            if x >> j & 1:
                continue
            break
        y = x | (1 << j)
        for k in range(j):
            y &= ~(1 << k)
        y |= 1 << i
        a.append(y)
    print(a[-1])


if __name__ == "__main__":
    main()
